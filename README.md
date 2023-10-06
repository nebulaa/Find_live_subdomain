# Find Live Subdomains

This Python script allows you to find live subdomains for a specified domain using the SecurityTrails API. It sends API requests to retrieve subdomains associated with the given domain and then checks the HTTP response status code for each subdomain to determine if it is live or not. The results are saved to a text file.

## Prerequisites

Before using this script, make sure you have the following:

1. Python 3 installed on your system.
2. Required Python libraries installed. You can install them using `pip`:
   ```
   pip install requests tqdm
   ```

## Getting Started

1. Clone or download this repository to your local machine.

2. Obtain an API key from [SecurityTrails](https://securitytrails.com/). You will need to replace `"ENTER_YOUR_API_KEY_HERE"` in the script with your actual API key.

3. Run the script:
   ```
   python get_sub_domain.py
   ```

4. Follow the prompts:
   - Enter the domain name for which you want to find subdomains.
   - Specify the output filename to save the list of subdomains along with their response codes.

5. The script will fetch subdomains, check their response codes, and save the results in a text file.

## Usage

You can use this script to quickly discover live subdomains for a given domain. The results will be saved in a text file for further analysis or enumeration.

## Example

Here's an example of how to run the script:

```shell
python get_sub_domain.py

Enter Domain name to find its sub-domains: example.com
Output Filename to save all domain names from API response: subdomains.txt
```

After execution, the live subdomains and their response codes will be saved in a file named `example.com_response_code.txt`.

## Note

- Use this script responsibly and only on domains you have permission to scan.
- Make sure to replace `"ENTER_YOUR_API_KEY_HERE"` with your actual SecurityTrails API key.
- The script utilizes multiprocessing to speed up the scanning process. Adjust the `timeout` parameter in the `get_resp` function to control the request timeout.
