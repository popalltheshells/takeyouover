import subprocess

def run_dnsrecon(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            domain = line.strip()
            if domain:
                dnsrecon_command = f"dnsrecon -d {domain}"
                try:
                    dnsrecon_result = subprocess.run(dnsrecon_command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    for output_line in dnsrecon_result.stdout.splitlines():
                        if output_line.startswith("[-] DNSSEC is not configured for"):
                            # Run the dig command for the domain
                            dig_command = f"dig CNAME {domain}"
                            dig_result = subprocess.run(dig_command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            if "NXDOMAIN" in dig_result.stdout:
                                # Re-run dnsrecon if NXDOMAIN is found
                                rerun_dnsrecon_result = subprocess.run(dnsrecon_command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                # Filter and print specific output with domain
                                for rerun_output_line in rerun_dnsrecon_result.stdout.splitlines():
                                    if rerun_output_line.startswith("[*]      A"):
                                        print(f"{domain}: {rerun_output_line}")  # Print domain with the output line
                except subprocess.CalledProcessError as e:
                    print(f"An error occurred: {e.stderr}")

run_dnsrecon('list.txt')
