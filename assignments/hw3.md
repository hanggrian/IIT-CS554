# [Homework 3](https://github.com/hendraanggrian/IIT-CS554/blob/assets/assignments/hw3.pdf): SCANNS Indexing & Search

> You are to read the [SCANNS paper](http://datasys.cs.iit.edu/publications/2022_CCGrid22-SCANNS.pdf)
  that discusses in detail the indexing and search that is at the core of the
  *XSearch* system, which in turn was used to implement the *GIGI/MEMO*
  blockchain Proof of Space.
>
> Your review must be written in a narrative form, with bullets when
  appropriate. You are to generate a PDF file and submit it on BB before the
  deadline. You must do these reviews individually.

## Problem 1

> Paper title, paper authors, publication venue (conference, workshop, or
  journal name), year of publication.

Here's a citation block in APA format:

<div style="font-family: 'Noto Serif'; text-align: right;">
Chard, K., Giannakou, A., Orhean, A. I., Raicu, I., Ramakrishnan, L. (2022). <i>SCANNS: Towards Scalable and Concurrent Data Indexing and Searching in High-End Computing System</i>. http://datasys.cs.iit.edu/publications/2022_CCGrid22-SCANNS.pdf
</div>

## Problem 2

> Paper summary (150~300 words); Clearly state the nature of the work (e.g.
  implementation of a real system, simulation, theoretical, empirical
  performance evaluation, survey, etc).

Searches and indexing are integral parts of modern applications. Global
internet search traffic is controlled by *Google*, but the enterprise search
market remains largely uncaptured. See, unlike web search engines that only need
to parse HTML files, searching in an enterprise environment requires
compatibility for all proprietary documents and integration into third-party
services.<sup>[\[1\]]</sup> It all boils down to how unstructured the companies
keep their computer files. However, their file structure and storing strategy
may be crucial to them, thus we should not race toward disrupting their
workflow. Enterprise search is also anticipated to operate in parallel since
these important files are usually located across multiple systems.

To tackle this issue, researchers from the *Illinois Institute of Technology*,
*Lawrence Berkeley National Lab*, and the *University of Chicago* have teamed up
to create a search framework codenamed SCANNS. When creating SCANNS, they are
particularly attentive to the scalability and modularity aspect of the search
engine framework while still achieving high performance as the primary goal. For
example, they opt to use state-of-the-art server components to execute their
limited tests. Moreover, they are adamant to support interchangeable NUMA nodes
from the get-go.

Woefully, NUMA architecture is not a one-shot solution to address the memory
latency bottleneck since only certain use cases will benefit from the unified
memory access it provides. This is all too apparent in many customized variants
of SCANNS, some of which are related to NUMA configuration.<sup>[\[2\]]</sup>

## Problem 3

> What are the core contributions of this paper (1~3 items)?

1. **Embrace unified memory**: NUMA nodes are here to stay in HPC for their
  modularity and scalability. Unlike conventional clusters, they are not known
  to have bandwidth issues within their inter-nodal links.
2. **Optimize every operation**: Performance advancement in enterprise search
  often requires tuning in specific areas. In SCANNS' case, the file reader and
  tokenizer have been heavily modified.
3. **Highly experimental**: Currently a work in progress, but still yields
  impressive results within the restrictive environment.

## Problem 4

> How is this work/solution different than related work (<300 words)?

Long before SCANNS was introduced, a [CNET](https://www.cnet.com/) employee was
working on a search functionality for the company website.<sup>[\[5\]]</sup>
This project would go on to become [Apache Solr](https://solr.apache.org/), the
most popular open-source search platform today and a worthy comparable to
SCANNS.<sup>[\[3\]]</sup> Unfortunately, Solr, being almost 20 years old, is not well-equipped to
leverage high-end hardware found in modern HPC. Most of it boils down to the
inclusion of their unsupported in-house search library [Apache Lucene](https://lucene.apache.org/).<sup>[\[4\]]</sup>

The development of SCANNS took a distinct approach. Having the advantage of
being written from the ground up, SCANNS never had to incorporate Lucene and can
run on newer hardware like NVMe drives. SCANNS have indexing, querying, mapping,
and ranking mechanism, as standard procedures for search platforms. However,
what is particularly unique about SCANNS is the implementation of said elements
is built with efficiency in mind with *DualQueue* design. It also successfully
reaches a faster transfer rate with a custom string delimiter, inverted
indexing, and direct disk read through *ReaderDriver*.

SCANNS also faces competition from cloud-based search platforms like [Amazon Kendra](https://aws.amazon.com/kendra/) and [Coveo](https://www.coveo.com/en). Being a conventional
framework, SCANNS expects the maintainer to do all the configuration work while
Coveo rapidly gains popularity due to its streamlined experience. Another
peculiar area that online enterprise search engines are good at is artificial
intelligence.<sup>[\[6\]]</sup> Being backed by large corporate, it is no
surprise that they are ahead in research and marketing.

## Problem 5

> Pros: Identify 3 things that this paper does well.

1. **Not all about hardware**: The paper acknowledges that the indexing
  algorithm also plays an important role to reach the maximum potential of any
  given hardware.
2. **Benchmarking many variants**: The authors experiment with numerous builds
  to evaluate how well each optimization is doing.
3. **Development insights**: The authors spent an adequate amount of time
  talking about current development progress and the roadmap for what lies
  ahead. In this instance, they explore the possibility of persistent indexing
  using Intel Optane DC drives.

## Problem 6

> Cons: Identify 3 things that this paper could do better.

1. **Deceptively advertised facts**: The figure up to 19&times; faster indexing
  and 280&times; lower search latency are backed up by extremely selective data.
2. **Unmeaningful gain with commodity hardware**: Peak performance is only
  realistic using high-end components typically found in server stacks rather
  than home desktops. This is a criticism of the technology rather than the
  paper itself, but the paper could shed some light on it.
3. **Code and licensing**: There is no information on source code repository and
  licensing. I believe they are required to, since they use [libnuma](https://github.com/numactl/numactl/),
  a GNU-licensed library.

## Problem 7

> Identify 1 thing that the author could do that would make the paper better.

The paper contains a few descriptive graphs displaying the inner working of
SCANNS' designs like DualQueue and ReaderDrive. Nevertheless, I argue there
needs to be more graphics depicting how the network deployment of SCANNS is
different compared to the existing Apache Lucene-based platforms, considering
they use sharding instead of NUMA nodes.

## Problem 8

> Identify 1 thing that someone could pursue as future work (that is not
  identified in the paper already).

As an off-topic work, the paper could inspect the use of semantic search in
enterprise networks. Semantic search refers to linguistic modeling to form
lexical indexing based on individual words rather than full context.

This is purely speculation, I have no way of knowing if SCANNS has already
integrated semantic searching into the search algorithm. I just can't find the
details in the *Ranking Algorithm* section.

## References

1. [Mukherjee, R., & Mao, J. (2004). *Enterprise Search: Tough Stuff: Why is it that searching an intranet is so much harder than searching the Web?*. Queue, 2(2), 36-46.](https://dl.acm.org/doi/pdf/10.1145/988392.988406/)
2. [Lameter, C. (2013). *NUMA (Non-Uniform Memory Access): An Overview: NUMA becomes more common because memory controllers get close to execution units on microprocessors*. Queue, 11(7), 40-51.](https://dl.acm.org/doi/pdf/10.1145/2508834.2513149/)
3. [Smiley, D., Mitchell, M., Parisa, K., Pugh, E. (2015). *Apache Solr Enterprise Search Server - Third Edition*. United Kingdom: Packt Publishing.](https://www.google.com/books/edition/_/u6GrCQAAQBAJ/)
4. [Balipa, M., & Balasubramani, R. (2015). *Search engine using apache lucene*. International Journal of Computer Applications, 127(9), 27-30.](https://www.researchgate.net/profile/Balasubramani-Ramasamy/publication/283771724_Search_Engine_using_Apache_Lucene/links/5b90bb6845851540d1d12d14/Search-Engine-using-Apache-Lucene.pdf)
5. [Medium: What is Apache Solr](https://johnthuma.medium.com/what-is-apache-solr-a18a60004e70/)
6. [Computerworld: How to choose an enterprise search platform](https://www.computerworld.com/article/3655951/how-to-choose-an-enterprise-search-platform.html)
7. [Digitalthoughts: Semantic Search: Understanding the Technology and Its Significance in New Age Enterprise Search](https://blog.thedigitalgroup.com/semantic-search-understanding-the-technology-and-its-significance-in-new-age-enterprise-search/)

[\[1\]]: https://dl.acm.org/doi/pdf/10.1145/988392.988406/
[\[2\]]: https://dl.acm.org/doi/pdf/10.1145/2508834.2513149/
[\[3\]]: https://www.google.com/books/edition/_/u6GrCQAAQBAJ/
[\[4\]]: https://www.researchgate.net/profile/Balasubramani-Ramasamy/publication/283771724_Search_Engine_using_Apache_Lucene/links/5b90bb6845851540d1d12d14/Search-Engine-using-Apache-Lucene.pdf
[\[5\]]: https://johnthuma.medium.com/what-is-apache-solr-a18a60004e70/
[\[6\]]: https://www.computerworld.com/article/3655951/how-to-choose-an-enterprise-search-platform.html
[\[7\]]: https://blog.thedigitalgroup.com/semantic-search-understanding-the-technology-and-its-significance-in-new-age-enterprise-search/
