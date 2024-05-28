docker scout cves --only-severity critical,high --exit-code zadanie2test:latest
echo "SCAN_RESULT=$?" >> "$GITHUB_ENV"