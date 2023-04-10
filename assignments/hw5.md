# [Homework 5](https://github.com/hendraanggrian/IIT-CS554/blob/assets/assignments/hw5.pdf): BLAKE Hash Function

> You are to read the [BLAKE3 paper](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)
  that discusses in detail the BLAKE3 cryptographic hashing algorithm and its
  performance compared to SHA256 as well as other cryptographic hashing
  algorithms.
>
> Your review must be written in a narrative form, with bullets when
  appropriate. You are to generate a PDF file and submit it on BB before the
  deadline. You must do these reviews individually.

## Problem 1

> Paper title, paper authors, publication venue (conference, workshop, or
  journal name), year of publication.

Here's a citation block in APA format:

<div style="font-family: 'Noto Serif'; text-align: right;">
Aumasson, J. P., O'Connor, J., Neves, S., Wilcox-O'Hearn, Z. (2021). <i>BLAKE3: one function, fast everywhere</i>. https://github.com/BLAKE3-team/BLAKE3-specs/raw/master/blake3.pdf
</div>

## Problem 2

> Paper summary (150~300 words); Clearly state the nature of the work (e.g.
  implementation of a real system, simulation, theoretical, empirical
  performance evaluation, survey, etc).

Cryptographic hashing &ndash; not to be confused with encrypting &ndash; is a
one-way ciphering of digital information (mostly texts) through various
techniques. Hash functions are expected to produce the same results while still
being collision resistance, that is, it should be next to impossible to find 2
inputs with the same output.<sup>[\[1\]]</sup> In an era where consumer data
passes freely between networks, obfuscating unintended materials is crucial to
maintain the privacy of our society. This is one of the premises that led to the
creation of the 2007 cryptographic hash function competition funded by the US
*National Institute of Standards and Technology* (NIST), in which BLAKE
participated.

BLAKE achieves cryptographic hashes by utilizing a symmetric key cipher.
Throughout the contest, BLAKE was rigorously inspected and tested by the leading
analysts in the cryptographic fields. The early version of BLAKE exceled in
performance and cost from the get-go.<sup>[\[2\]]</sup> And though BLAKE also
performed well in security and complexity, *Keccak* ultimately won the race for
its ideal structures and designs. Keccak is implemented into *SHA-3* according
to the rules agreed upon.<sup>[\[7\]]</sup>

Despite this, the development of BLAKE continues and picked up steam with the
release of their first major update BLAKE2. Several improvements are made to
increase the performance, one of them being partial parallel hashing.<sup>[\[3\]]</sup>
The speed boost that comes with this decision is often regarded as the primary
reason for its newfound popularity. BLAKE3 has extended this property by
announcing unrestricted parallelism through its in-house binary tree structure,
effectively surpassing the industry standard *SHA-256* in the documented tests.

## Problem 3

> What are the core contributions of this paper (1~3 items)?

1. **Embracing parallelism**: Supports an unrestricted amount of parallel
  computing, resulting in up to 12 times faster hashing when deployed in
  multi-threaded systems.
2. **Benchmarking BLAKE3**: Shows scientific data and graphical context on how
  far BLAKE has improved over the years by comparing it to previous iterations.
3. **Progressive thinking**: Believing that the current state of cryptography is
  too conservative, BLAKE3 reduces the number of rounds from 10 to 7.<sup>[\[4\]]</sup>

## Problem 4

> How is this work/solution different than related work (<300 words)?

Subsequently, after the declaration of the SHA-3 competition, NIST has received
dozens of applications from corporates, scholars, and hobbyists alike from
around the world. Each applicant has a unique approach and design philosophy,
which in turn affects its performance and reliability. One of the participants
is [Fugue](https://researcher.watson.ibm.com/researcher/view_group.php?id=3302),
an IBM-backed project which narrowly missed the final stage. But of all the
candidates who did not pass, perhaps the most disappointing is *MD6*. It is a
successor to *MD5*, a wildly popular hash function that is also the basis of
*checksum*.

NIST named 5 competitors in the third and final round of the SHA-3 competition:
BLAKE, *Grostl*, *JH*, Keccak, and *Skein*.<sup>[\[5\]]</sup> Skein features
modified symmetric key ciphers that can accept additional input, they are called
tweakable block ciphers.<sup>[\[6\]]</sup> In contrast, Keccak employed a sponge
construction paradigm where the hashes can self-grow or recede depending on the
requirement. This extended flexibility could be attributed to its eventual
victory over other contenders.

Since the competition has concluded well over a decade ago, there are emerging
hash functions such as *Bcrypt*, *Password-Based Key Derivation Function 2*
(PBKDF2) and *Scrypt*.<sup>[\[8\]]</sup> However, they are specifically designed
for password hashing rather than general use.

## Problem 5

> Pros: Identify 3 things that this paper does well.

1. **Stay on scope**: BLAKE3 has undergone many transformations during its
  development cycles, nevertheless hashing speed remains the top priority.
2. **Uphold flexibility**: The authors describe ways that BLAKE3 is
  collision-resistant, therefore making it suitable for any purpose.
3. **Deep insights**: Section Rationales extensively explain the reasoning
  behind every important design decision that makes up BLAKE3.

## Problem 6

> Cons: Identify 3 things that this paper could do better.

1. **Unconventional formatting**: For example, there is no conclusion section, a
  common element of any academic paper.
2. **Limited comparison models**: Only *SHA* and *KangarooTwelve* are selected
  to be measured for their performance against variants of BLAKE.
3. **Doesn't talk about ASIC**: It is well reported that BLAKE struggles in
  *Application-Specific Integration Circuit*, the paper just flat-out ignored
  it.<sup>[\[9\]]</sup>

## Problem 7

> Identify 1 thing that the author could do that would make the paper better.

I cannot find a good reason in this paper or online for why the authors decided
to write BLAKE3 in *Rust* instead of previously *C*, I honestly think it is a
piece of information worth sharing. I'm not trying to diss Rust, I'm sure it is
a capable programming language. It's just that this kind of decision need to be
properly documented.

## Problem 8

> Identify 1 thing that someone could pursue as future work (that is not
  identified in the paper already).

As a future work, the paper could discuss the current phenomenon of hashing
algorithms: we keep relying on increased digest size to avoid a collision.<sup>[\[10\]]</sup>
Pretty soon when this strategy stops working &ndash; for example, when quantum
computing becomes mainstream &ndash; the whole foundation of hash function
security is at risk of dramatically changing. But to be completely fair to the
authors, this topic is inherently related to the universal hash function instead
of singling out BLAKE.

## References

1. [Al-Kuwari, S., Davenport, J. H., & Bradford, R. J. (2011). *Cryptographic hash functions: Recent design trends and security notions*. Cryptology ePrint Archive.](https://eprint.iacr.org/2011/565.pdf)
2. [Al Shaikhli, I., Alahmad, M., & Munthir, K. (2014). *Hash function of finalist SHA-3: Analysis study*. International Journal of Advanced Computer Science and Information Technology (IJACSIT) Vol, 2, 1-12.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2376182)
3. [Aumasson, J. P., Neves, S., Wilcox-O’Hearn, Z., & Winnerlein, C. (2013). *BLAKE2: simpler, smaller, fast as MD5*. In Applied Cryptography and Network Security: 11th International Conference, ACNS 2013, Banff, AB, Canada, June 25-28, 2013. Proceedings 11 (pp. 119-135). Springer Berlin Heidelberg.](https://eprint.iacr.org/2013/322.pdf)
4. [Aumasson, J. P. (2019). *Too much crypto*. Cryptology ePrint Archive.](https://eprint.iacr.org/2019/1492.pdf)
5. [Chang, S. J., Perlner, R., Burr, W. E., Turan, M. S., Kelsey, J. M., Paul, S., & Bassham, L. E. (2012). *Third-round report of the SHA-3 cryptographic hash algorithm competition*. NIST Interagency Report, 7896, 121.](https://nvlpubs.nist.gov/nistpubs/ir/2012/NIST.IR.7896.pdf)
6. [Liskov, M., Rivest, R. L., & Wagner, D. (2002). *Tweakable block ciphers*. In Advances in Cryptology—CRYPTO 2002: 22nd Annual International Cryptology Conference Santa Barbara, California, USA, August 18–22, 2002 Proceedings 22 (pp. 31-46). Springer Berlin Heidelberg.](https://home.cs.colorado.edu/~jrblack/class/csci7000/f03/papers/tweak-crypto02.pdf)
7. [NIST: NIST Selects Winner of Secure Hash Algorithm (SHA-3) Competition](https://www.nist.gov/news-events/news/2012/10/nist-selects-winner-secure-hash-algorithm-sha-3-competition/)
8. [The Guardian: Passwords and hacking: the jargon of hashing, salting and SHA-2 explained](https://www.theguardian.com/technology/2016/dec/15/passwords-hacking-hashing-salting-sha-2/)
9. [StackExchange Cryptography: What advantages does Keccak/SHA-3 have over BLAKE2?](https://crypto.stackexchange.com/questions/31674/what-advantages-does-keccak-sha-3-have-over-blake2/)
10. [Medium: The State of Hashing Algorithms — The Why, The How, and The Future](https://medium.com/@rauljordan/the-state-of-hashing-algorithms-the-why-the-how-and-the-future-b21d5c0440de/)

[\[1\]]: https://eprint.iacr.org/2011/565.pdf
[\[2\]]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2376182
[\[3\]]: https://eprint.iacr.org/2013/322.pdf
[\[4\]]: https://eprint.iacr.org/2019/1492.pdf
[\[5\]]: https://nvlpubs.nist.gov/nistpubs/ir/2012/NIST.IR.7896.pdf
[\[6\]]: https://home.cs.colorado.edu/~jrblack/class/csci7000/f03/papers/tweak-crypto02.pdf
[\[7\]]: https://www.nist.gov/news-events/news/2012/10/nist-selects-winner-secure-hash-algorithm-sha-3-competition/
[\[8\]]: https://www.theguardian.com/technology/2016/dec/15/passwords-hacking-hashing-salting-sha-2/
[\[9\]]: https://crypto.stackexchange.com/questions/31674/what-advantages-does-keccak-sha-3-have-over-blake2/
[\[10\]]: https://medium.com/@rauljordan/the-state-of-hashing-algorithms-the-why-the-how-and-the-future-b21d5c0440de/
