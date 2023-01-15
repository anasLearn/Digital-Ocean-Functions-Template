When in production, create inside this folder a file *config.ini*

The file must have the following format (remove the stars `*`):

```markdown
[MERCH]
TOKEN = *vendhq token*
DOMAIN_PREFIX = *vendhq domain prefix*

[SMS]
SID = *twilio account sid*
TOKEN = *twilio account token*

[NUMBERS]
N1 = *first number*
N2 = *2nd number*

\# Add as many lines as needed
```