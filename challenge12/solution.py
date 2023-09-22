rules:
    - id: python-debugger-true
      languages:
        - python
      message: Detected debug true
      severity: WARNING
      patterns:
        - pattern: $APP.debug=True
