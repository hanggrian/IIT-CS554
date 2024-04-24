# [Project proposal](https://github.com/hendraanggrian/IIT-CS554/blob/assets/assignments/proj.pdf): Plot compression in *Chia* blockchain

### *Abstract*

*Chia is a blockchain-based cryptocurrency that uses Proof of Space and Time
(PoST) consensus mechanism. The PoST requires the farmer to show that they have
allocated a certain amount of disk space over a period of time to be eligible to
create a new block. The process of allocating disk space is known as plotting,
and Chia allows for different levels of plot compression (0-7) to reduce the
amount of disk space required for plotting. This project aims to compare the
different levels of plot compression in terms of their impact on farming speed
and storage efficiency.<sup>[\[2\]]</sup>*

## Introduction

Chia is a relatively new cryptocurrency that has gained significant attention
due to its eco-friendliness and energy efficiency compared to other popular
cryptocurrencies like *Bitcoin*. Chia uses a novel consensus algorithm called
proof-of-space-and-time (PoST), which requires farmers to allocate disk space to
store plot files that contain pre-computed solutions to a cryptographic puzzle.
The plot files are then used to generate proofs of space that are submitted to
the network to participate in the consensus process.<sup>[\[1\]]</sup>

Plot compression is an important aspect of Chia farming, as it determines the
size of the plot files on disk and affects the overall efficiency and
profitability of farming. Plot compression reduces the size of plot files by
eliminating redundant data and compressing the remaining data using a
compression algorithm. There are seven levels of plot compression available in
Chia, each with varying degrees of compression and processing time.

Being a community that strives for power efficiency as Chia is, compression is
unsurprisingly already supported in existing plots dating back to 2020. However,
the current state of plot compression is shrinking data using a standard
lossless compression algorithm. This paper instead acknowledge that plot
compression refers to deliberate removal of integral parts of a block in effort
to reduce its file size, they are later required to be recreated at the cost of
extra computing power.<sup>[\[3\]]</sup>

This approach is unfortunately not a perfect one, as the storage save is linear
while the power increase is exponential for each level of compression. To combat
this issue, Chia and the community behind the movement have released a series of
solutions that leverage other parts of the computer.<sup>[\[4\]]</sup>

## Compression strategy

### Use GPU

GPU plotting relies on a dedicated graphic card instead of a CPU. This is
particularly a good news because modern graphics cards are usually more than
adequate enough for Chia plotting, with most of the restrictions being either
raw GPU performance, PCIe bandwidth, or memory bandwidth.<sup>[\[5\]]</sup>

There are a few implementations around, the most famous being [Chia Gigahorse](https://github.com/madMAx43v3r/chia-gigahorse/) by *madMAx*. Chia later published their version of GPU plotting
with [BladeBit CUDA](https://github.com/Chia-Network/bladebit/tree/cuda-compression).
Unfortunately, like madMAx's implementation, Nvidia cards with CUDA capability
are necessary, this essentially means no AMD cards, or at least not yet.

### Use RAM or storage

The term *BladeBit* also refers to [BladeBit Disk](https://github.com/Chia-Network/bladebit),
a separate software that leverages in-memory or mainstream storage devices
instead computing power like CPU and GPU. It has been reported that the high
performance of this disk-based plotting is even faster than its GPU equivalent.

However, it require hundreds of GigaBytes of RAM or storage, making it only
accessible on workstations and servers.

## Timelines

Starting at **March 24th, 2023**.

Week # | Deliverable
---: | ---
1 | Run tests on all compression levels.
2 | Explore the possibility of using GPU or RAM plotting.
3 | Prepare final report.
**4** | **Final Presentation.**

## Conclusions

The aim of this project is to compare the different levels of plot compression
in Chia and determine their impact on farming speed, storage efficiency, energy
consumption, and savings-to-consumption ratio. The research will provide
insights into the optimal level of plot compression for Chia farmers to use,
considering performance, storage, and energy requirements.

## References

1.  [Agrawal, S. (2022, June 4). *Secure Plot Transfer for the Chia Blockchain*.](https://eprint.iacr.org/2022/871.pdf)
1.  [Cohen, B., Pietrzak, K., (2019, July 9). *The Chia Network Blockchain*.
    Chia Network. IST Austria.](https://www.chivescoin.org/wp-content/uploads/2021/10/ChiaGreenPaper.pdf)
1.  [Chia News: Plotting Chia's Future](https://www.chia.net/2023/01/20/plotting-chias-future/)
1.  [Chia News: Plot compression is here](https://www.chia.net/2023/01/20/plot-compression-is-here/)
1.  [Chia News: GPU Plotting is Real – and Very Fast](https://www.chia.net/2023/01/20/gpu-plotting-is-real---and-very-fast/)
1.  [Chia Forum: Few facts about "compressed plot"](https://chiaforum.com/t/few-facts-about-compressed-plot/18336/6/)

[\[1\]]: https://eprint.iacr.org/2022/871.pdf
[\[2\]]: https://www.chivescoin.org/wp-content/uploads/2021/10/ChiaGreenPaper.pdf
[\[3\]]: https://www.chia.net/2023/01/20/plotting-chias-future/
[\[4\]]: https://www.chia.net/2023/01/20/plot-compression-is-here/
[\[5\]]: https://www.chia.net/2023/01/20/gpu-plotting-is-real---and-very-fast/
[\[6\]]: https://chiaforum.com/t/few-facts-about-compressed-plot/18336/6/
