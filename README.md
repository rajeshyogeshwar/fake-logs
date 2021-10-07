# fake-logs

fake-logs is a fake logs generator command line tool as well as a package that can be imported and used within the python code.

### Inspiration

While learning Apache Kafka, I wanted to play around with huge volume of data and I also wanted to generate it. So I wrote this one.

### Usage?

##### Command Line

If you intend to use CLI below are the available CLI options. CLI is provide to generate a log file with large number of records efficiently.

    Usage: fake-logs [OPTIONS]
    Options:

    -e, --engine [nginx|apache-common|apache-combined] Option to define tool for which to generate logs. [required]
    -l, --lines INTEGER Number of log lines. [required]
    -i, --interval FLOAT Interval between consecutive logs.
    -f, --file_path TEXT Absolute file path to write logs to.[required]

    --help Show this message and exit.

##### As a python package

If you intend to import this as a dependency in your project. You can generate logs in following way.

    from generator import get_nginx_webserver_log, get_apache_webserver_log

    # Nginx Combined Log Format
    nginx_log = get_nginx_webserver_log(interval=1)
    for _ in range(50):
        print(next(nginx_log))

    # Apache Webserver Common Log Format
    apache_common_format_log = get_apache_webserver_log(interval=1, format="common")
    for _ in range(50):
        print(next(apache_common_format_log))

    # Apache Webserver Combined Log Format
    apache_combined_format_log = get_apache_webserver_log(interval=1, format="combined")
    for _ in range(50):
        print(next(apache_combined_format_log))

`get_nginx_webserver_log` and `get_apache_webserver_log` are both generators and they take care of maintaining the interval between two consecutive logs.

### Performance

```
![alt text](https://raw.githubusercontent.com/rajeshyogeshwar/fake-logs/main/images/perf.png)
```
