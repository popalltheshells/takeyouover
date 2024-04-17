# Takeyouover

This project presents a Python-based automation tool designed to enhance penetration testing workflows specifically focusing on the detection of vulnerable subdomains that could be susceptible to takeover attacks. By leveraging dnsrecon for initial reconnaissance and dig commands to verify DNS configurations, the tool efficiently identifies domains that lack DNSSEC protection and checks for NXDOMAIN responses which signal potential vulnerabilities.

The key feature of this tool is its ability to automatically rerun reconnaissance on domains that exhibit signs of weak security settings, particularly those that might lead to subdomain takeovers. This automated, iterative approach ensures thorough validation and helps security teams quickly pinpoint critical vulnerabilities across their domain infrastructure.
