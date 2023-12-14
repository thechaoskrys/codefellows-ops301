# Import the Active Directory module
Import-Module ActiveDirectory

# Define user information
$FirstName = "Franz"
$LastName = "Ferdinand"
$DisplayName = "$FirstName $LastName"
$SamAccountName = "ferdinandf"
$UserPrincipalName = "$SamAccountName@GlobeXpower.com"
$Title = "TPS Reporting Lead"
$Department = "TPS Department"
$Office = "Springfield, OR"
$Company = "GlobeX USA"
$Email = "ferdi@GlobeXpower.com"
$Password = "P@ssw0rd"  # You should set a secure password here

# Create a secure password
$SecurePassword = ConvertTo-SecureString -String $Password -AsPlainText -Force

# Specify the organizational unit (OU) where the user will be created
$OrganizationalUnit = "OU=Users,DC=contoso,DC=com"  # Update with your actual domain information

# Create the user in Active Directory
New-ADUser -SamAccountName $SamAccountName -UserPrincipalName $UserPrincipalName -Name $DisplayName -GivenName $FirstName -Surname $LastName -DisplayName $DisplayName -Title $Title -Department $Department -Office $Office -Company $Company -EmailAddress $Email -Enabled $true -AccountPassword $SecurePassword -Path $OrganizationalUnit

# References 
# ChatGPT conversation: https://chat.openai.com/share/363ad4c3-251e-4dad-8659-8f780ede2223