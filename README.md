# Takeyouover

Still missing a few features. For now, please run ``` whois <IP> | grep "OrgName" ``` on the results of this script, then you'll be able to takeover the subdomain.

**Usage**: Please make sure the list of subdomains are in a file called list.txt, and within the same directory as this script.

``` python3 takeyouover.py ```

This project presents a Python-based automation tool designed to enhance penetration testing workflows specifically focusing on the detection of vulnerable subdomains that could be susceptible to takeover attacks. By leveraging dnsrecon for initial reconnaissance and dig commands to verify DNS configurations, the tool efficiently identifies domains that lack DNSSEC protection and checks for NXDOMAIN responses which signal potential vulnerabilities.

For more details; https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/10-Test_for_Subdomain_Takeover


The key feature of this tool is its ability to automatically rerun reconnaissance on domains that exhibit signs of weak security settings, particularly those that might lead to subdomain takeovers. This automated, iterative approach ensures thorough validation and helps security teams quickly pinpoint critical vulnerabilities across their domain infrastructure.
