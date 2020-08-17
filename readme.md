# Connectwise Manage - Change all Company Names to Title Case

## Usage

### Connectwise Manage 

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
.\changeCompanyName.ps1
```

