---
layout: wiki
---

PSL uses [SLF4J](http://www.slf4j.org/) for logging. In the PSL Groovy program template, SLF4J is bound to Log4j 1.2. The Log4j configuration file is located at `src/main/resources/log4j.properties`. It should look something like this:

```
# Set root logger level to the designated level and its only appender to A1.
log4j.rootLogger=ERROR, A1

# A1 is set to be a ConsoleAppender.
log4j.appender.A1=org.apache.log4j.ConsoleAppender

# A1 uses PatternLayout.
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=%-4r [%t] %-5p %c %x - %m%n
```

The logging verbosity can be set by changing `ERROR` in the second line to a different level and recompiling. Options include `OFF`, `WARN`, `DEBUG`, and `TRACE`.