# Hyper-V Auditing

## Usage

### Hyper-V output CPU, RAM, SSD usage

on Hyper-V server (tested on server02 and server03)

```
.\Get-HyperVReport.ps1 -Cluster P1-CL01
```

open myoutput.txt to get results

### Connectwise Manage output Agreement Additions for CPU, RAM, SSD 

first enter your creds for Connectwise Manage in password.ps1

next

```
.\additionsAudit.ps1
```

results returned to console
