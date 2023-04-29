# [Project Presentation](https://github.com/hendraanggrian/IIT-CS554/blob/assets/assignments/proj_presentation.pdf): Plot compression in *Chia* blockchain

Phases: https://www.chia.net/wp-content/uploads/2023/01/proof_of_space.pdf

## Group

![Slide 1](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide1.png)

## Introduction 1

![Slide 2](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide2.png)

## Introduction 2

![Slide 3](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide3.png)

## Introduction 3

![Slide 4](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide4.png)

## Background

![Slide 5](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide5.png)

## Motivation

![Slide 6](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide6.png)

## Proposed Solution

![Slide 7](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide7.png)

- We propose test results using commodity hardware.
  - This personal desktop lies in between the minimum and recommended system
    requirements from official Chia documentation.
  - The boot drive is where OS and Chia application are. Chia will use this to
    store the internal database, so SSD is recommended.
- It is tested against 3 plotters my colleague has explained all of them.
- The temporary directory and final directory are prompted for each plot.

## Evaluation 1

![Slide 8](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide8.png)

- The first phase is what they called forward-propagating.
- During this process, they are creating temporary files with. Different plotter
  generates temporary files with different pattern. The graphic you see here is
  the pattern used by official plotter.
- In this phase, the farmer also creates and locks the final plot file. It is
  marked by tmp file extension.

## Evaluation 2

![Slide 9](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide9.png)

- In the second stage, they scan the last 6 tables, sort them and keep the
  sorted keys in a column.
- The documentation also says that they remove unused data, but I cannot see
  what they removed from the logs.

## Evaluation 3

![Slide 10](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide10.png)

- The third phase is all about compression.
- All tables change from a column-based system to double-pointers.
- The performance of this task and log messages are identical to stage 2.

## Evaluation 4

![Slide 11](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide11.png)

- In the last phase, there are always 16 buckets for bucket sort.
- What is interesting about this phase is Chia automatically checks if your
  hardware has sufficient RAM for these buckets. If not, they will store them
  persistently.
- Those buckets will then write the final plot file, and release the file lock.

## Evaluation 5

![Slide 12](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide12.png)

- Over here are our findings, down below there are two `k25` plots, done in
  about 2-3 minutes.
- While `k32`, the most common plot size, is around 12 hours.
- Phase 4, which involves optional RAM, is unsurprisingly the fastest.
- As you can see, some of them are unfinished. I did not foresee that it
  would take 12 hours for each test, and they cannot be executed in parallel.
- But if you follow the pattern, you can expect about 1-2 hours of saving.

## Related work

![Slide 13](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide13.png)

## Conclusion 1

![Slide 14](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide14.png)

## Conclusion 2

![Slide 15](https://github.com/hendraanggrian/IIT-CS554/raw/assets/bladebit-research/slide15.png)

- In future work, we could leverage other hardware such as RAM and GPU.
- Both Chia and madMAx are strict about NVIDIA requirements.
- But they are more accessible than the 400GB RAM requirement here.
