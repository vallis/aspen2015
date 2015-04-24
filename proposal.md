# Physical insight at the crossroads of computation, systematics, and inference: the case of gravitational-wave detection with millisecond-pulsar timing

## A proposal for a 2015 Aspen summer program

## Organizers

* Michele Vallisneri (Jet Propulsion Laboratory, Michele.Vallisneri@jpl.nasa.gov)
* Andrea Lommen (Franklin and Marshall, andrea.lommen@fandm.edu)
* Xavi Siemens (University of Wisconsin, siemens@gravity.phys.uwm.edu)
* Michael Kramer (Max Planck Institute for Radio Astronomy, Bonn, michael@mpifr-bonn.mpg.de)

## Synopsis

The _precision timing of an array of millisecond pulsars_ across several years offers the opportunity of searching for low-frequency (nHz) gravitational waves (GWs), which appear as correlated modulations in the times of arrival of the radio pulses.
Possible sources include supermassive black-hole binaries at the centers of merged galaxies (either observed individually, or as a stochastic ensemble signal), bursts or backgrounds from cosmic strings, early-Universe events, and more.
Although the idea of GW detection by pulsar timing is thirty years old, it has received much attention in recent years as improvements in receiver hardware and the discovery of new "good-timer" pulsars have made the prospect of an actual GW detection tantalizingly close (see Figure 1). Three international consortia (NANOGrav in north America, the EPTA in Europe, and the PPTA in Australia) have formed to collect and analyze timing data for this purpose. The three consortia later joined in the International Pulsar Timing Array (IPTA), which integrates data and coordinates joint analyses.

While the principle and practice of deriving _timing solutions_ (the deterministic, non-GW effect on the times of arrival) and of searching timing data for GWs are well established [see the recent reviews in the CQG focus issue 30 (2013)], we must push deeper in three crucial research directions (_computation_, _systematics_, and _inference_) before we can achieve the first GW detection with its full scientific payoff.
While these themes have very specific applications in the case of pulsar timing, many other areas of modern astronomy and astrophysics face the same issues:

* How do we apply our _computational resources_ optimally to extract the _maximum information_ from the data?
* How do we model systematic effects so that we can truly _believe what we conclude_?
* How do we design the most _powerful and robust representation for the astrophysical information_ that we gain from an observation?

![Figure 1, left: projected 95%-confidence NANOGrav upper limit and 50%- and 90%-confidence detection level for a stochastic signal from supermassive-black-hole binaries; as more data are accumulated, the curves scope out the gray parameter region expected from population estimates. The solid/dashed curves correspond to optimistic/conservative assumptions about neutron-star spin noise. Right: projected sensitivity to monochromatic GWs from individual resolvable binaries. (Courtesy of Xavier Siemens, NANOGrav.)](roadmap.png)

Thus, we propose an Aspen program that would focus on these general problems for the specific example of GW detection with pulsar timing. The program would bring together pulsar-timing experts with specialists from other disciplines (such as CMB analysts, exoplanet observers, GW phenomenologists, and more) who search for weak signals in noisy data, and who have to deal with resource-limited computation, strong systematics, "deep" statistical inference, or all of the above. The resulting exchange of techniques and viewpoints would prove illuminating, in expected and unexpected ways, for all involved.

To wit, a robust GW-detection outcome with pulsar timing will require: 

1. The practical ability of running _efficient analyses_ of full IPTA-scale datasets (50+ pulsars over 10+ years), which requires advances in formalizing the searches, organizing the data, and implementing the algorithms on large parallel clusters.
2. A defensible control of _"data quality" issues and systematic effects_, as needed for data obtained from a variety of radiotelescopes using heterogeneous techniques, and for a detection technique that in effect relies on neutron stars (with all their physics and complexity) as fundamental clocks. For instance, "detector" models should include statistical characterizations of astrophysical noise effects in neutron stars, in their magnetospheres, and in the interstellar medium.
3. A sharp and principled understanding of the _astrophysical inferences and constraints_ that may be drawn from a detection (e.g., on black-hole populations and on black-hole merger and accretion history), and especially of how the model parametrization and implicit or explicit astrophysical priors affect our conclusions.

Without efficient computational implementations, we will not be able to explore the statistical significance of searches by running them repeatedly with different tunings. Without a strong handle on systematic effects, we will not be able to provide a fully convincing claim of detection, as highlighted by the recent debate over the BICEP2 results. Without a robust formulation for the astrophysical interpretation of a detection, our momentous discoveries will not feed back into our understanding of the Universe.
These topics are all undergoing energetic study and development by NANOGrav and its international partners, and are among the scientific targets proposed NSF Physics Frontiers Center and Mid-scale Innovation Program in Astronomy.
Nevertheless, they would benefit in a major and unique way from the focused attention and unstructured collaboration made possible by an Aspen Summer program.

By the end of the program, the sum of our scientific exchanges will amount to 
tentative but concrete answers to our two most pressing questions: "How do we convince the world and ourselves that these are really GWs and not instrumental, non-GW-astrophysical, or pulsar effects?"; and "How do we structure formal astrophysical inferences from these data?"
<!-- The organizers would take the responsibility of capturing the results of these exercises and making them available to the larger community. -->
To help their reflections, the participants would be able (but by no means required!) to run statistical and numerical experiments on actual IPTA datasets containing simulated GW signals and systematic effects of various types and levels. The experiments would be facilitated by tools and example data prepared by the organizers and their teams in advance of the program.

We believe that the scientific results of our proposed program, as well as the lasting relationships and collaborations that would be created between participants, would be invaluable to the international GW-detection-by-pulsar-timing community, but also to all non-pulsar-timing participants. Furthermore, the topic of the program (the detection of GWs, using general-relativistic objects as detectors) makes it especially suited to programming in 2015, which marks the centenary of the theory of general relativity. 

## Scheduling ##

The desired length of the program is 3 to 4 weeks.

Scheduling note: we are aware of another 2015 summer-program proposal, led by our colleague Sean McWilliams, which would study supermassive black-hole astrophysics and its relations with low-frequency GW astronomy. That program and our proposed program would be very complementary (and yet appeal to mostly distinct communities), and we would welcome them to be scheduled in partial concurrence should both be approved (similar to the overlapping studies in 2014 on the topics of compact binaries and gamma-ray bursts/kilonovae).

Scheduling conflicts: the 2015 IPTA summer school and science meeting will take place in Australia, probably June 29-July 3 and July 6-10 respectively (to be confirmed). Two major GW meetings, which pose less of a conflict, will take place in June: the Gravitational-wave Physics and Astronomy Workshop in Osaka, Japan (6/17-20), and the Eleventh Edoardo Amaldi Conference on Gravitational Waves in Gwangju, Korea (6/21-26).

Organizer availability: Vallisneri and Lommen have children in school, and their availability may be limited in the last week of May 2015, and after mid-August 2015. Kramer will be at a general-relativity meeting in Germany at the end of May, and at the IAU general assembly on August 3-14, 2015.

Preferred weeks: any weeks between June 1 and August 14, with the exception of July 6-10 (if the IPTA meeting is confirmed for those dates). May and August 17 and later are very difficult.

## Organizers responsible for diversity ##

Michele Vallisneri and Andrea Lommen

## Possible participants ##

This proposal has been developed in collaboration with Joseph Lazio, Rutger van Haasteren, Justin Ellis, Steven Taylor (all JPL) and Chiara Mingarelli (Caltech) who should be considered key participants. In addition, the following researchers have communicated their interest (or we are rather sure they would be interested):

* Stas Babak (AEI, Golm)
* Jim Cordes (Cornell)
* Neil Cornish (Montana)
* Paul Demorest (NRAO)
* Roseanne Di Stefano (CfA)
* Olivier Doré (JPL)
* Daniel Foreman-Mackey (NYU)
* George Hobbs (ATNF)
* David Hogg (NYU)
* Jeffrey Jewell (JPL)
* K. J. Lee (MPIfR)
* Rick Jenet (UTB)
* Vicki Kaspi (McGill)
* Michael Keith (Jodrell Bank CfA)
* Matthew Kerr (CSIRO)
* Patrick Lazarus (MPIfR, Bonn)
* Lindley Lentati (Cambridge)
* Yuri Levin (Monash)
* Dustin Madison (Cornell)
* Walid Majid (JPL)
* Ilya Mandel (Birmingham)
* Maura McLaughlin (WVU)
* Sean McWilliams (WVU)
* Chris Messenger (SUPA, Glasgow)
* Jean-Michel Desert (Boulder)
* David Nice (Lafayette)
* Antoine Petiteau (Université Paris-Diderot)
* Reinhard Prix (AEI, Hannover)
* Scott Ransom (NRAO)
* Paul Ray (NRL)
* Daniel Reardon (Monash)
* Joe Romano (UTB)
* Ryan Shannon (CSIRO)
* Ingrid Stairs (UBC)
* Dan Stinebring (Oberlin)
* Alberto Vecchio (University of Birmingham)
* Jingbo Wang (ATNF)
* Linqing Wen (University of Western Australia)
* Karl Wette (AEI, Hannover)
* Xingjiang Zhu (University of Western Australia)