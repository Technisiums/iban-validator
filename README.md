# IBAN Validator
### Montenegro's IBANs
 Currently, API only supports Validation of Montenegro's IBANs.
 #### Endpoint
```text
/api/validate_iban?iban={MontengeroIBAN}
```
some of the valid IBANs are listed below to tests

|          IBAN          | Valid / Invalid |
|:----------------------:|:---------------:|
| ME59234342312345654213 |      Valid      |
| ME59234342319845654217 |     Invalid     |
| ME32234342312234124390 |      Valid      |
| ME59234342312345654982 |     Invalid     |
| ME38567098765789765745 |      Valid      |
