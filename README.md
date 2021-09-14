## API HostName

通过 API 的方式提供给 IP_Crawler 项目调用。

具体返回结果示例：

~~~
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": false,
  "CD": false,
  "Question": [
    {
      "name": "233.202.249.110.in-addr.arpa.",
      "type": 12
    }
  ],
  "Answer": [
    {
      "name": "233.202.249.110.in-addr.arpa.",
      "type": 12,
      "TTL": 600,
      "data": "bytespider-110-249-202-233.crawl.bytedance.com."
    }
  ],
  "Comment": "Response from 61.55.134.132."
}
~~~

无结果的返回示例：

~~~
{
  "Status": 3,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "35.35.124.221.in-addr.arpa.",
      "type": 12
    }
  ],
  "Authority": [
    {
      "name": "221.in-addr.arpa.",
      "type": 6,
      "TTL": 1070,
      "data": "ns.apnic.net. read-txt-record-of-zone-first-dns-admin.apnic.net. 3006087948 7200 1800 604800 3600"
    }
  ]
}
~~~