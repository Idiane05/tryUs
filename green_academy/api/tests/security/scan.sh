#!/bin/bash
# Run OWASP ZAP scan
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-weekly zap-baseline.py \
  -t http://localhost:8000 -r security_report.html