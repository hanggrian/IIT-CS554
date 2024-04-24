<!-- hotfix: KaTeX -->
<!-- https://github.com/yzane/vscode-markdown-pdf/issues/21/ -->
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">MathJax.Hub.Config({ tex2jax: { inlineMath: [['$', '$']] }, messageStyle: 'none' });</script>

# Homework 6: *XSearch* time-based storage

> You are to read the [XSearch paper](http://datasys.cs.iit.edu/publications/2018_IIT-oral-xsearch.pdf).
>
> Your review must be written in a narrative form, with bullets when
  appropriate. You are to generate a PDF file and submit it on BB before the
  deadline. You must do these reviews individually.

## Problem 1

> Paper title, paper authors, publication venue (conference, workshop, or
  journal name), year of publication.

Here's a citation block in APA format:

<div style="font-family: 'Noto Serif'; text-align: right;">
Nguyen, L., Raicu, I., (2018). <i>XSearch: Distributed Information Retrieval in
Large-Scale Storage Systems</i>.
http://datasys.cs.iit.edu/publications/2018_IIT-oral-xsearch.pdf
</div>

## Problem 2

> Paper summary (150~300 words); Clearly state the nature of the work (e.g.
  implementation of a real system, simulation, theoretical, empirical
  performance evaluation, survey, etc).

In an increasingly digital era, storing entries into a database in a
conventional manner such as integer indices and unique strings no longer
suffice. Growing complexity and precision usually resolve to slower create,
read, update, and delete (CRUD) execution time. With many advancements that
popular database vendors the likes of *MongoDB* and *InfluxDB*, they are yet to
achieve $O(1)$ time when the sample size is worth decades of data.

XStore is a storage framework that centers around using chronological value as
the mapping key. They are then classified by year and organized within the
`dataStore` compound. Much of what makes this approach possible is the sparse
file implementation, a special file type that stretches itself when necessary.
XStore is designed to run on multiple hardware in a networking layer, as to
maintain the level of scalability. After setting up, XStore is then ready to
feed the data to the client via the [ZeroMQ](https://zeromq.org/) protocol.

## Problem 3

> What are the core contributions of this paper (1~3 items)?

- Introduce a new time-based indexing mechanism.
- Guarantees linear CRUD operations in a large-scale scenario.
- All while having a lower carbon footprint than leading databases like MongoDB.

## Problem 4

> How is this work/solution different than related work (<300 words)?

MongoDB supports using chronology as an identifier of documents out-of-the-box,
at least to a certain degree. See, in MongoDB, each document is normally backed
by a helper file inaccessible to end users.<sup>[\[1\]]</sup>

As a *Relational Database Management System (RDBMS)*, InfluxDB also supports a
time-scale storage system. However, comparing against it would not be a fair
challenge as XStore is only intended for NoSQL.<sup>[\[2\]]</sup>

## Problem 5

> Pros: Identify 3 things that this paper does well.

- High-precision granularity when querying CRUD commands in persistent disks.
- Extensive test cases that make up for plentiful statistics as showcased in
  *Figure 12: Benchmark - Unary Insert*.
- Unlike Hadoop which was initially for commodity computers, XStore supports
  HPC.

## Problem 6

> Cons: Identify 3 things that this paper could do better.

- Could have been compared against more database vendors, particularly from
  large entities such as *Amazon Cassandra* or *Apache HBase*.
- XStore performance claim is not spread across all configurations. Sequential
  operations, for instance, are comparable to those of MongoDB tests.
- Unproven in a real-world environment, all test results attached in the paper
  are executed in the cloud.

## Problem 7

> Identify 1 thing that the author could do that would make the paper better.

By positioning itself towards high-performance computing, XStore is essentially
inaccessible for most hobbyists and enthusiasts with commodity hardware. This is
a clear loss, a low barrier brings community, which may help in testing and
documentation in a later stage, even if XStore decides it is going to be
closed-source later.

## Problem 8

> Identify 1 thing that someone could pursue as future work (that is not
  identified in the paper already).

As a future work, XStore should consider leveraging in-memory storage for
temporary caching. I understand this goes against the core philosophy, but I
believe database maintainers should have options. Certain maintainers go to
extreme lengths utilizing in-memory support in their MongoDB databases with
*Redis*, there is an untapped potential here.

## References

1.  [(2021). *MongoDB Architecture Guide*. MongoDB, Inc.](http://s3.amazonaws.com/info-mongodb-com/MongoDB_Architecture_Guide.pdf)
1.  [Naqvi, S. N. Z., Yfantidou, S., & Zimányi, E. (2017). Time series databases
    and influxdb. Studienarbeit, Université Libre de Bruxelles, 12.](https://www.devopsschool.com/blog/wp-content/uploads/2022/09/influxdb_2017.pdf)

[\[1\]]: http://s3.amazonaws.com/info-mongodb-com/MongoDB_Architecture_Guide.pdf
[\[2\]]: https://www.devopsschool.com/blog/wp-content/uploads/2022/09/influxdb_2017.pdf
