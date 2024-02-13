# waves over lambda
### AUTHOR: INVISIBILITY/DANNY
### Challlenge Points: 300

## Category
Cryptography
## Challenge Description
We made alot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 13758`.
## Hints
Flag is not in the usual flag format
## Solution

The problem statement tells us that substitutions were used in encrypting this. After connecting with the host, we get a lot of gibberish:

console```
root@kali:/Cryptography/waves-over-lambda# nc jupiter.challenges.picoctf.org 13758
-------------------------------------------------------------------------------
scdqpxhf uapa jf ectp bixq - bpaytadse_jf_s_cnap_ixrmgx_gdnhbphxet
-------------------------------------------------------------------------------
uxnjdq uxg fcra hjra xh re gjfocfxi luad jd icdgcd, j uxg njfjhag hua mpjhjfu rtfatr, xdg rxga faxpsu xrcdq hua mccwf xdg rxof jd hua ijmpxpe paqxpgjdq hpxdfeinxdjx; jh uxg fhptsw ra huxh fcra bcpawdcliagqa cb hua sctdhpe sctig uxpgie bxji hc uxna fcra jrocphxdsa jd gaxijdq ljhu x dcmiarxd cb huxh sctdhpe. j bjdg huxh hua gjfhpjsh ua dxrag jf jd hua azhpara axfh cb hua sctdhpe, ktfh cd hua mcpgapf cb hupaa fhxhaf, hpxdfeinxdjx, rcigxnjx xdg mtwcnjdx, jd hua rjgfh cb hua sxpoxhujxd rctdhxjdf; cda cb hua ljigafh xdg iaxfh wdcld ocphjcdf cb atpcoa. j lxf dch xmia hc ijquh cd xde rxo cp lcpw qjnjdq hua azxsh icsxijhe cb hua sxfhia gpxstix, xf huapa xpa dc rxof cb hujf sctdhpe xf eah hc scroxpa ljhu ctp cld cpgdxdsa ftpnae rxof; mth j bctdg huxh mjfhpjhv, hua ocfh hcld dxrag me sctdh gpxstix, jf x bxjpie laii-wdcld oixsa. j fuxii adhap uapa fcra cb re dchaf, xf huae rxe pabpafu re rarcpe luad j hxiw cnap re hpxnaif ljhu rjdx.
```

On this occasion, searching for a plain-text word like picoCTF wasn't feasible since the flag doesn't adhere to the typical format. However, we have the option to utilize a tool such as [DCODE](https://www.dcode.fr/monoalphabetic-substitution) to resolve this issue. Initially, we'll consider monoalphabetic substitution as our potential encryption method, wherein each character is substituted with another. DCODE offers an automated decryption feature that scans for coherent English messages, thus providing us with the flag.

## Flag
`FREQUENCY_IS_C_OVER_LAMBDA_DNVTFRTAYU`