# Hyper-V Auditing

## Usage

### Hyper-V output CPU, RAM, SSD usage

on Hyper-V server (tested on server02 and server03)

```
.\Get-HyperVReport.ps1 -Cluster P1-CL01
```

open myoutput.txt to get results

to sum up values per client

```
python sum.py
```

results returned to console

### Connectwise Manage output Agreement Additions for CPU, RAM, SSD 

first enter your creds for Connectwise Manage in password.ps1

```
$myServer = "au.myconnectwise.net"
$myCompany = "XXXXXXXXXXXX" #company name
$mypubkey = "XXXXXXXXXXXXXXXX" #login to Manage > My Account > API keys
$myprivatekey = "XXXXXXXXXXXXXXXX" #login to Manage > My Account > API keys
$myclientId = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" #register and generate clientId here https://developer.connectwise.com/ClientID
$username = "XXXX" #username to login to Manage
$password = "XXXXXXXXXXXX" #password to login to Manage
 ```

next

```
.\additionsAudit.ps1
```

results returned to console
