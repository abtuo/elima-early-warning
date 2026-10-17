# Security policy

## Supported versions

This project is an early prototype. Security fixes are applied to the latest version on the
`main` branch; older releases are not maintained separately.

## Reporting a vulnerability

Report vulnerabilities privately to <contact@elima.africa>. Include a minimal, anonymized
reproduction, affected version, and likely impact. Do not include personal data, learner
records, credentials, or other secrets. Please allow maintainers time to investigate before
public disclosure.

## Deployment warning

The demonstration service has no authentication, authorization, rate limiting, audit log,
or secure data persistence. Do not expose it directly to the public internet or submit real
learner records. Any deployment requires appropriate transport security, access controls,
monitoring, retention rules, and incident-response procedures.
