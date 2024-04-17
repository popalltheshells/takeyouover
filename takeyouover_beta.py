#untested

import subprocess

def read_domains(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def run_dnsrecon(domain):
    dnsrecon_command = f"dnsrecon -d {domain}"
    try:
        result = subprocess.run(dnsrecon_command, shell=True, check=True, text=True, stdout=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running dnsrecon on {domain}: {e}")
        return ""

def check_cname_records(domain, subdomain):
    dig_command = f"dig CNAME {subdomain}"
    try:
        result = subprocess.run(dig_command, shell=True, check=True, text=True, stdout=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error checking CNAME for {subdomain}: {e}")
        return ""

def get_whois(ip):
    whois_command = f"whois {ip} | grep 'OrgName'"
    try:
        result = subprocess.run(whois_command, shell=True, check=True, text=True, stdout=subprocess.PIPE)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error performing whois on {ip}: {e}")
        return ""

def analyze_dnsrecon_output(output):
    lines = output.split('\n')
    for line in lines:
        if "DNSSEC is not configured" in line or "NXDOMAIN" in line:
            print(line)
        if line.startswith("[*]      A"):
            ip = line.split()[-1]
            org_name = get_whois(ip)
            print(f"{line} - {org_name}")
        if line.startswith("[*]      CNAME"):
            cname_record = line.split()[-1]
            dig_result = check_cname_records(cname_record.split()[0], cname_record)
            print(f"{line} - CNAME check result: {dig_result}")

def main():
    domains = read_domains("list.txt")
    for domain in domains:
        print(f"Testing {domain}...")
        dnsrecon_output = run_dnsrecon(domain)
        analyze_dnsrecon_output(dnsrecon_output)

if __name__ == "__main__":
    main()
