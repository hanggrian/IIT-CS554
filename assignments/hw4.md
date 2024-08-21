# [Homework 4](https://github.com/hanggrian/IIT-CS554/blob/assets/assignments/hw4.pdf): *LINPACK* Benchmark

> You are to read the 2003 [LINPACK paper](https://onlinelibrary.wiley.com/doi/pdf/10.1002/cpe.728)
  that discusses in detail the Linpack Benchmark, which has been used for
  decades to create the [Top 500 ranking](https://www.top500.org).
>
> Your review must be written in a narrative form, with bullets when
  appropriate. You are to generate a PDF file and submit it on BB before the
  deadline. You must do these reviews individually.

## Problem 1

> Paper title, paper authors, publication venue (conference, workshop, or
  journal name), year of publication.

Here's a citation block in APA format:

<div style="font-family: 'Noto Serif'; text-align: right;">
Dongarra, J. J., Luszczek, P., & Petitet, A. (2003). <i>The LINPACK Benchmark:
Past, present and future</i>. Concurrency and Computation: Practice and
Experience. https://doi.org/10.1002/cpe.728
</div>

## Problem 2

> Paper summary (150~300 words); Clearly state the nature of the work (e.g.
  implementation of a real system, simulation, theoretical, empirical
  performance evaluation, survey, etc).

A supercomputer is described as a cluster of interconnected computers with
state-of-the-art performance far surpassing the level of general-purpose
consumer PCs or even enterprise-grade servers.<sup>[\[4\]]</sup> This extreme
speed &mdash; usually measured in floating-point operations per second (FLOPS)
&mdash; is traditionally reserved for intensive workloads in highly specific
areas like scientific modeling and physics simulation. Most notably and
recently, the supercomputer has been able to break the petaFLOPS barrier in the
21st century, news well received by the parallel computing community.

However, present-day high-performance computing (HPC) introduces new challenges
such as heterogeneous CPU architecture (*Itanium*, *ARM*, etc.), complexity of
third-party applications, and many aspects to a lesser extent.<sup>[\[5\]]</sup>
HPC hardware components are often hand-picked and custom-built on account that
they only need to perform a limited set of tasks (but pass with flying colors).
And therein lies the biggest dilemma of benchmarking HPC: utter lack of
standardization in the sea of diverse HPCs.

*Jack Dongarra* proposed the *LINPACK benchmark* tool in 1979 to tackle this
issue. Unlike commercial benchmark software like *3DMark* or *Cinebench*,
LINPACK has a reduced scope of only measuring floating-point computing power.
LINPACK relies on single-precision and double-precision equation routines to
produce accurate results.<sup>[\[1\]]</sup> As time went on, various
improvements are made and new variants are established. Since its inception, the
main project has branched out into several configurations like *LINPACK 100*,
*LINPACK 1000*, and *HPLinpack*. LINPACK benchmarks would go on to feature in
the infamous non-profit [TOP500 Supercomputer](https://www.top500.org/) list.
Nowadays LINPACK is superseded by *LAPACK*, which boasts a newer linear algebra
package.<sup>[\[6\]]</sup>

## Problem 3

> What are the core contributions of this paper (1~3 items)?

1.  **Started as a mathematical library:** LINPACK was first published as
    Fortran executables calculating linear algebra problems. It drew inspiration
    from another package called BLAS.
1.  **Established methodology of HPC benchmarking:** The analysis of theoretical
    peak and efficiency rate is still the basis of benchmarking today.
1.  **Predicting the future of the benchmark:** The authors make an educated
    guess of how the upcoming benchmark tool would look based on the trends of
    that time.

## Problem 4

> How is this work/solution different than related work (<300 words)?

An obvious comparison to the *High-Performance Linpack (HPL)* is the
*High-Performance Conjugate Gradient (HPCG)*, another project of Jack Dongarra
himself. HPCG was first conceived out of a relatable concern that the HPL
benchmark outcome is growing increasingly ambiguous, that is, scoring high no
longer necessarily means equitable real-world performance.<sup>[\[2\]]</sup> To
stay relevant in the supercomputer ecosystem, HPCG decided to incorporate more
constraints namely memory access and recursive calculation speed in the pattern
they call **Type 2**. However, it should be noted that HPCG is designed to be
light enough to run in tandem with HPL as a complementary benchmark rather than
a full-blown replacement.

There is also a kernel-based approach with Fast Fourier transform (FTT)
algorithm which excels in signal processing. Unfortunately, it offers no
meaningful performance impact over HPCG while still running at a low-efficiency
rate.<sup>[\[3\]]</sup> With these characteristics in mind, the FFT-based
benchmark is deemed a less attractive replacement.

In the end, HPL remains an important supercomputer benchmarking tool albeit with
reduced relevancy.<sup>[\[4\]]</sup> It sets the standard of the early
supercomputer benchmarking model. But more importantly, it serves as an
inspiration to the existing and future generations of benchmark tools to come.

## Problem 5

> Pros: Identify 3 things that this paper does well.

1.  **Historical context:** Gives insight into how LINPACK is first created by
    an accident and stays a passion project.
1.  **Classifying variants:** There are 4 separate LINPACK benchmarks
    categorized by matrix dimension and other optimizations. The authors
    understand that one configuration cannot satisfy every requirement.
1.  **Naturally humble:** When describing its inclusion into the TOP500
    Supercomputer list, the authors acknowledge that the importance of such
    honor is diminishing.

## Problem 6

> Cons: Identify 3 things that this paper could do better.

1.  **Incomplete tables:** Though there are 4 variants available, only
    *LINPACK 100* is consistently being used as a test case.
1.  **Naive expectations:** It is apparent in the conclusion that the paper
    expects Moore's Law would uphold in the foreseeable future.
    This prediction would end up being wrong.
1.  **Not perfect as is:** For example, the paper has admitted that vector
    operations are expected to experience hiccups in unconfigured HPC.

## Problem 7

> Identify 1 thing that the author could do that would make the paper better.

I would bring the HPCG benchmark into the discussion, particularly in the
section on the Future of the Benchmark. I understand that HPCG was created much
later, but this LINPACK paper is the more recent version released in 2003. By
that time, HPCG is already well-known to the community.

## Problem 8

> Identify 1 thing that someone could pursue as future work (that is not
  identified in the paper already).

One overlooked topic of the paper is GPU's role in supercomputers, especially
the ones that are specifically tuned for HPC like [Nvidia Tesla](https://www.nvidia.com/en-us/data-center/data-center-gpus/)
or [AMD Radeon Instinct](https://www.amd.com/en/graphics/instinct-server-accelerators/).
Granted, introduction of GPU in HPC further complicate the state of
benchmarking. But GPUs will inevitably occupy HPC space since they considerably
cost less (performance per dollar and watt) and may unlock new possibilities.<sup>[\[7\]]</sup>

## References

1.  [Dongarra, J. J. (2005, May). *The LINPACK benchmark: An explanation*. In
    Supercomputing: 1st International Conference Athens, Greece, June 8–12, 1987
    Proceedings (pp. 456-474). Berlin, Heidelberg: Springer Berlin Heidelberg.](https://link.springer.com/chapter/10.1007/3-540-18991-2_27/)
1.  [Heroux, M. A., & Dongarra, J. (2013). *Toward a new metric for ranking high
    performance computing systems (No. SAND2013-4744)*. Sandia National
    Lab.(SNL-NM), Albuquerque, NM (United States); University of Tennessee,,
    Knoxville, TN.](https://www.osti.gov/servlets/purl/1089988/)
1.  [None, N. (2016). *Performance, Efficiency, and Effectiveness of
    Supercomputers* (No. SAND2016-12782). Sandia National Lab.(SNL-NM),
    Albuquerque, NM (United States).](https://www.osti.gov/servlets/purl/1505370/)
1.  [ZDNET: The rise, fall, and rise of the supercomputer in the cloud era](https://www.zdnet.com/article/the-rise-fall-and-rise-of-the-supercomputer-in-the-cloud-era/)
1.  [ZDNET: NASA gets SGI 2048-core Itanium 2 supercomputer](https://www.zdnet.com/article/nasa-gets-sgi-2048-core-itanium-2-supercomputer/)
1.  [ZDNET: ​Supercomputers: All Linux, all the time](https://www.zdnet.com/article/supercomputers-all-linux-all-the-time/)
1.  [TheRegister: What should replace Linpack for ranking supercomputers?](https://www.theregister.com/2013/06/21/hpcg_supercomputing_benchmark_proposal/)

[\[1\]]: https://link.springer.com/chapter/10.1007/3-540-18991-2_27/
[\[2\]]: https://www.osti.gov/servlets/purl/1089988/
[\[3\]]: https://www.osti.gov/servlets/purl/1505370/
[\[4\]]: https://www.zdnet.com/article/the-rise-fall-and-rise-of-the-supercomputer-in-the-cloud-era/
[\[5\]]: https://www.zdnet.com/article/nasa-gets-sgi-2048-core-itanium-2-supercomputer/
[\[6\]]: https://www.zdnet.com/article/supercomputers-all-linux-all-the-time/
[\[7\]]: https://www.theregister.com/2013/06/21/hpcg_supercomputing_benchmark_proposal/
