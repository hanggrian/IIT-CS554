# [Project presentation](https://github.com/hendraanggrian/IIT-CS554/blob/assets/assignments/proj_presentation.pdf): Plot compression in *Chia* blockchain

Phases: https://www.chia.net/wp-content/uploads/2023/01/proof_of_space.pdf

## Group

![Slide 1](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide1.png)

## Introduction 1

![Slide 2](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide2.png)

> Partner's part.

## Introduction 2

![Slide 3](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide3.png)

> Partner's part.

## Introduction 3

![Slide 4](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide4.png)

> Partner's part.

## Background

![Slide 5](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide5.png)

> Partner's part.

## Motivation

![Slide 6](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide6.png)

> Partner's part.

## Proposed Solution

![Slide 7](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide7.png)

- We propose test results using commodity hardware.
  - This personal desktop lies in between the minimum and recommended system
    requirements from official Chia documentation.
  - The boot drive is where OS and Chia application are. Chia will use this to
    store the internal database, so SSD is recommended.
- It is tested against 3 plotters my colleague has explained all of them.
- The temporary directory and final directory are prompted for each plot.

## Evaluation 1

![Slide 8](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide8.png)

- The first phase is what they called forward-propagating.
- During this process, they are creating temporary files with. Different plotter
  generates temporary files with different pattern. The graphic you see here is
  the pattern used by official plotter.
- In this phase, the farmer also creates and locks the final plot file. It is
  marked by tmp file extension.

## Evaluation 2

![Slide 9](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide9.png)

- In the second stage, they scan the last 6 tables, sort them and keep the
  sorted keys in a column.
- The documentation also says that they remove unused data, but I cannot see
  what they removed from the logs.

## Evaluation 3

![Slide 10](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide10.png)

- The third phase is all about compression.
- All tables change from a column-based system to double-pointers.
- The performance of this task and log messages are identical to stage 2.

## Evaluation 4

![Slide 11](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide11.png)

- In the last phase, there are always 16 buckets for bucket sort.
- What is interesting about this phase is Chia automatically checks if your
  hardware has sufficient RAM for these buckets. If not, they will store them
  persistently.
- Those buckets will then write the final plot file, and release the file lock.

## Evaluation 5

![Slide 12](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide12.png)

- Over here are our findings, down below there are two `k25` plots, done in
  about 2-3 minutes.
- While `k32`, the most common plot size, is around 12 hours.
- Phase 4, which involves optional RAM, is unsurprisingly the fastest.
- As you can see, some of them are unfinished. I did not foresee that it
  would take 12 hours for each test, and they cannot be executed in parallel.
- But if you follow the pattern, you can expect about 1-2 hours of saving.

## Related work

![Slide 13](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide13.png)

> Partner's part.

## Conclusion 1

![Slide 14](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide14.png)

> Partner's part.

## Conclusion 2

![Slide 15](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit/slide15.png)

- In future work, we could leverage other hardware such as RAM and GPU.
- Both Chia and madMAx are strict about NVIDIA requirements.
- But they are more accessible than the 400GB RAM requirement here.
