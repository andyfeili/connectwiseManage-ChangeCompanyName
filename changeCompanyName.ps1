Import-Module .\CWManage.psm1
Import-Module .\password.ps1
	
	function Start-CWMConnection
	{
		# This is the URL to your manage server.
		$Server = $myServer

		# This is the company entered at login
		$Company = $myCompany

		#Public and private key created in connectwise manage
		$pubkey = $mypubkey
		$privatekey = $myprivatekey

		#ClientID created from https://developer.connectwise.com/ClientID
		$clientId = $myclientId


		# Connect to Manage server
		$Connection = @{
					Server = $Server
					Company = $Company 
					pubkey = $pubkey
					privatekey = $privatekey
					clientId = $clientId
				}
		Connect-CWM @Connection
		Write-Output "Authenticated successfully with Manage"
	} 

Start-CWMConnection

$allcompany = Get-CWMCompany -all

foreach($entry in $allcompany){

	$name = $entry.name
	$name = $name.toLower()
	$TextInfo = (Get-Culture).TextInfo
	$NewName = $TextInfo.ToTitleCase($name)

	$UpdateParam = @{

		CompanyID = $entry.id
		Operation = 'replace'
		Path = 'name'
		Value = $NewName
	}
Update-CWMCompany @UpdateParam
}
