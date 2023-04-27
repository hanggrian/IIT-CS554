# [Project](https://github.com/hendraanggrian/IIT-CS554/blob/assets/assignments/prof_final.pdf): Plot compression in *Chia* blockchain

### *Abstract*

## Introduction

Since its inception in 2008, Bitcoin &mdash; and in turn, the cryptocurrency
movement &mdash; has amassed millions of users across the globe. This trend has
exponentially raised the value of digital coins while emitting massive amounts
of pollution in the process, and it shows no sign of slowing down. Much of the
power hogging is attributed to the consensus model of the blockchain, it
verifies transactions and dictates how new coins are generated.<sup>[\[2\]]</sup>

In a conventional cryptocurrency, such as Bitcoin and Litecoin, proof-of-work
remains the de-facto protocol. Proof-of-work operates by giving the participants
sets of complex mathematical questions that require extreme precision and lots
of computing power. By constantly competing for the fastest and accurate answer,
the system has proved that it is statistically improbable (or financially
unappealing) for a bad actor to manipulate or recreate the blockchain.

### The downfall of proof-of-work

For a proof-of-work mechanism to stay robust in a growing market, it would
require a propotional amount of energy and electricity bills. In 2022, it has
reached a point where the global electricity usage of cryptocurrencies has
surpassed the total annual electricity of countries such as Argentina or
Australia. With the increasing popularity of digital assets, the power needed to
run them is expected to exceed the entire traditional servers around the world.<sup>[\[6\]]</sup>

With Bitcoin's heightening power consumption, it is inevitable that other and
often overlooked consensus models are on the rise. For example, proof-of-stake
first appeared as a hybrid implementation in a cryptocurrency now known as
*Peercoin*.<sup>[\[3\]]</sup> It only gained acknowledgment after *Ethereum*
fully utilized it in the long-awaited merge. Instead of solving arithmetic
problems, proof-of-stake relies on a voting arrangement where members with
higher stakes have a better chance of winning. It effectively eliminates small
players such as home miners from the competition as they are unable to match the
initial offerings of big organizations.<sup>[\[7\]]</sup>

## Overview of Chia

This led us to proof-of-space, a protocol of choice by Chia. Unlike the stakes
system, every attempt to participate in proof-of-space is connected to a
real-world object, which in this case, is storage.<sup>[\[8\]]</sup> This
property is inherently similar to proof-of-work, trading computing power for
storage. However, storage is deemed inexpensive, with prices continuing to
plummet.<sup>[\[9\]]</sup>

## Compression strategy

It is important to establish fundamentals about the type and extent of
compression before continuing further into advanced topics. First, there is a
lossless compression, that is, removed parts of the content do not affect the
desired result. For obvious reasons, this is a favored compression method that
has thus far been incorporated in Chia plots and activated by default.<sup>[\[10\]]</sup>

The other compression type, lossy compression, allows direct manipulation of the
result, to the extent that is agreed upon by the user, to maximize space saving.
In this paper, we explore various methods of lossy compression that are recently
introduced in the Chia ecosystem, either officially or third-party by the
community.

### Use GPU

Compression with a dedicated graphics card, though still in an experimental
phase, is already the fastest compression technique as the raw speed and memory
capacity of modern GPUs are currently in exponential growth. GPU also costs less
correlative to CPU while generating comparatively additional power. It is even
reported that GPUs with certain raw performance can expect bottlenecks with PCIe
or memory bandwidth.<sup>[\[11\]]</sup>

GPU plotting is initially supported in a community project known as Chia
Gigahorse by prominent member *madMAx*. Not long after, Chia chimes in with its
official implementation called *BladeBit*. Unfortunately in its current state,
compressing plots using GPU relies heavily on *CUDA* technology invented by
*NVIDIA*, thus hardware support is limited to the brand. And though support for
more GPU vendors is logged in the roadmap, there is no word on when it would be
available or its task priority within the team.

### Use RAM or storage

Lossy compression can alternatively be achieved with extra memory or storage.
This is a more accessible approach not only because both are cheaper than GPU,
but there is also no hardware constraint.

## Findings

## Conclusion

## References

1. [Cohen, B., & Pietrzak, K. (2019). *The chia network blockchain*. vol, 1, 1-44.](https://www.chivescoin.org/wp-content/uploads/2021/10/ChiaGreenPaper.pdf)
2. [Vranken, H. (2017). *Sustainability of bitcoin and blockchains*. Current opinion in environmental sustainability, 28, 1-9.](https://shop.tarjomeplus.com/UploadFileEn/TPLUS_EN_3047.pdf)
3. [King, S., & Nadal, S. (2012). *Ppcoin: Peer-to-peer crypto-currency with proof-of-stake*. self-published paper, August, 19(1).](https://www.peercoin.net/read/papers/peercoin-paper.pdf)
4. []()
5. []()
6. [The White House: FACT SHEET: Climate and Energy Implications of Crypto-Assets in the United States](https://www.whitehouse.gov/ostp/news-updates/2022/09/08/fact-sheet-climate-and-energy-implications-of-crypto-assets-in-the-united-states/)
7. [Ethereum: The Merge](https://ethereum.org/en/roadmap/merge/)
8. [Spacemesh: Proof of Stake vs Proof of Space Time](https://spacemesh.io/blog/proof-of-stake-vs-proof-of-space-time/)
9. [Tom's Hardware: How Low Can SSD Prices Go? TrendForce Expects NAND Price Decline to Continue](https://www.tomshardware.com/news/trendforce-expects-nand-flash-prices-to-continue-falling/)
10. [Chia News: Plotting Chia's Future](https://www.chia.net/2023/01/20/plotting-chias-future/)
11. [Chia News: GPU Plotting is Real – and Very Fast](https://www.chia.net/2023/01/20/gpu-plotting-is-real---and-very-fast/)

[\[1\]]: https://www.chivescoin.org/wp-content/uploads/2021/10/ChiaGreenPaper.pdf
[\[2\]]: https://shop.tarjomeplus.com/UploadFileEn/TPLUS_EN_3047.pdf
[\[3\]]: https://www.peercoin.net/read/papers/peercoin-paper.pdf
[\[4\]]:
[\[5\]]:
[\[6\]]: https://www.whitehouse.gov/ostp/news-updates/2022/09/08/fact-sheet-climate-and-energy-implications-of-crypto-assets-in-the-united-states/
[\[7\]]: https://ethereum.org/en/roadmap/merge/
[\[8\]]: https://spacemesh.io/blog/proof-of-stake-vs-proof-of-space-time/
[\[9\]]: https://www.tomshardware.com/news/trendforce-expects-nand-flash-prices-to-continue-falling/
[\[10\]]: https://www.chia.net/2023/01/20/plotting-chias-future/
[\[11\]]: https://www.chia.net/2023/01/20/gpu-plotting-is-real---and-very-fast/
