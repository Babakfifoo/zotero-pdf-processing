Journal of Housing Economics

# Developers' perspectives on timing to build: Evidence from microdata of land acquisition and development

Chien-Lin Lu[a](#page-0-0) , Wen-Chi Lia[ob,](#page-0-1)[⁎](#page-0-2) , Chien-Wen Peng[c](#page-0-3)

<span id="page-0-0"></span><sup>a</sup> *Department of Applied Economics and Management, National Ilan University, No. 1, Sec. 1, Shennong Rd., Yilan City, Yilan County 260, Taiwan*

<span id="page-0-1"></span><sup>b</sup> *Department of Real Estate, National University of Singapore, 21 Lower Kent Ridge Road, Singapore 119077, Singapore*

<span id="page-0-3"></span><sup>c</sup> *Department of Real Estate and Built Environment, National Taipei University, 151 University Rd., San Shia District, New Taipei City 23741, Taiwan*

#### ARTICLE INFO

*Keywords:* Accelerated failure time Land banking Real option Time to development Urban vacant land

*JEL codes:* L20 R14 R31 R52

#### ABSTRACT

The holding of vacant land has an option value. Existing theory reckons a linkage between the expected wait and the stochastic nature of development costs, but few empirical studies can address it due to data availability. This research merges developer characteristics with complete microdata on land acquisitions and developments of an emerging district in Taipei, and it adopts the Accelerated Failure Time model to examine the timing to build. The expected wait is longer for developers with more paid-in capital or with less development capacity. Most significantly, those involved in subsidiarization tend to shorten the wait. The results are robust under alternative specifications and consistent with the theoretical predictions of costs. Additionally, a policy incentive on the plot ratio substantially shortened the district's development process. The data have no censoring and truncation issues typically encountered in survival analysis. Further tests shed light on the severity of biases the estimation would suffer if the data had those issues.

#### **1. Introduction**

Land scarcity concerns urban planning authorities in large, growing cities. Coupled with continuous urbanization, it could worsen housing affordability and constrain the provision of land-intensive amenities and infrastructures. The issue can be overwhelming in the East (e.g., [Iwata and Oguchi, 2009](#page-15-0); [Kong, 2012](#page-15-1)), while it is also notable in the West (e.g., [Alig et al., 2004;](#page-14-0) [Asfour, 2012\)](#page-14-1). To mitigate, Asian city governments often attempt using government land sales to influence land supply.[1](#page-0-4)

However, lands are real options. Developers often wait and do not pursue immediate development after acquisition ([Titman, 1985](#page-15-2)), hindering a timely supply shift and causing problems of urban vacant land ([Mayer and Somerville, 2000](#page-15-3); [Quigley and Raphael, 2005\)](#page-15-4).[2](#page-0-5) Understanding the determinants of waiting can help the policy design of land supply, but empirical studies on the roles of developer characteristics are lacking. This paper researches developers' perspectives on the timing to build, merging microdata of real-estate developers, land acquisitions, and project developments.

Land development is irreversible, and its payoff is uncertain. Thus, the possibility to keep the land vacant and wait for the optimal timing to build creates an option value, which is the maximum of the expected return. A large volume of theoretical research has established the realoption theory and extended it to incorporate various angles of urban development [\(Titman, 1985](#page-15-2); [McDonald and Siegel, 1986](#page-15-5)[;Capozza and](#page-14-2) [Helsley, 1990;](#page-14-2) [Williams, 1991;](#page-15-6) [Capozza and Li, 1994](#page-14-3); [Wang and](#page-15-7) [Zhou, 2006;](#page-15-7) [Dong and Sing, 2017\)](#page-15-8). Particularly, [McDonald and](#page-15-5) [Siegel \(1986\)](#page-15-5) incorporate stochastic development costs as an important explaining factor.

Empirical research has confirmed that factors such as location, zoning, and competition can affect the option value, which significantly explains the price of the undeveloped land and the motivation to keep it vacant. [\(Quigg, 1993](#page-15-9); [Bulan et al., 2009](#page-14-4); [Guthrie, 2010](#page-15-10); [Grovenstein et al., 2011;](#page-15-11) [Tsekrekos and Kanoutos, 2013](#page-15-12); [Yang and](#page-15-13)

<span id="page-0-2"></span>⁎ Corresponding author.

<https://doi.org/10.1016/j.jhe.2020.101709>

Received 25 December 2018; Received in revised form 1 May 2020; Accepted 17 June 2020 Available online 20 June 2020 1051-1377/ © 2020 Elsevier Inc. All rights reserved.

*E-mail addresses:* [cllu@niu.edu.tw,](mailto:cllu@niu.edu.tw) [jacklu2004@hotmail.com](mailto:jacklu2004@hotmail.com) (C.-L. Lu), [wliao@nus.edu.sg](mailto:wliao@nus.edu.sg) (W.-C. Liao), [cwpeng@mail.ntpu.edu.tw](mailto:cwpeng@mail.ntpu.edu.tw) (C.-W. Peng).

<span id="page-0-4"></span><sup>1</sup> To assure adequate land supply, the Urban Redevelopment Authority of Singapore announces land sales through the Government Land Sales Programme (GLS) once every six months. The Land Department of Hong Kong has periodic GLS as well. The Taiwanese governments also administrate their land sales programs.

<span id="page-0-5"></span><sup>2</sup> Urban vacant land is a common problem in cities. For example, 28.7% and 14.2% of land plots were vacant in Orlando and San Diego in 1998, respectively [\(Pagano and Bowman, 2000](#page-15-14)). Even in New York City where land is precious, 5% of land plots were vacant, and 33% of these vacant lots were unused in 2011 [\(Kremer et al., 2013\)](#page-15-15).

<span id="page-1-0"></span>

**Fig. 1.** Background of National Taipei University District (NTPU-D)

# **Panel A: Map of NTPU-D**

#### **Panel B: Time trends of land auctions and developments in NTPU-D**

This figure shows the map of National Taipei University District (NTPU-D) and time trends of the 79 land auctions and developments acquired by private developers in NTPU-D from 2000 to 2011. Panel A marks the outskirt of NTPU-D with a solid line. The commercial district and National Taipei University is marked with a dashed line and dotted line, respectively. Panel B reports time trends of land auctions and developments. One parcel was acquired by a peasants' association in 2007 and thus excluded.

[Wu, 2019](#page-15-13)). Importantly, [Bulan et al. \(2009\)](#page-14-4) acknowledge the difficulty of obtaining development-cost data, which remains a significant gap in the empirical literature.

To fill this gap, we collect comprehensive information on the acquisitions and developments of all the land parcels in the National Taipei University District (NTPU-D), which was an urban redevelopment zone began in the 1990s and flourished in the 2000s, in Taiwan, as well as the characteristics of the developers holding these parcels. We apply an empirical survival model to estimate the hazard rate and make statistical inferences on how these developer characteristics relating to development costs affect the timing to build. The results are immune from the common censoring and truncation issues in survival analysis because the dataset consists of entire development processes of all lands.

Survival analysis is an appealing method to test the *time to develop*, which is the wait between the land acquisition and project launch because its results connect with the real-option theory well by the duality between the conditional probability and the first hitting-time of the development. The extant studies primarily concern macro-environmental factors. [Cunningham \(2006\)](#page-15-16) shows that uncertainty delays development, while [Bulan et al. \(2009\)](#page-14-4) find that competition negates this effect. [Groves \(2009\)](#page-15-17) and [Wrenn and Irwin \(2015\)](#page-15-18) evidence that property taxes and regulatory costs prolong the wait. [Wang et al. \(2016\)](#page-15-19) suggest that in China, policy uncertainty is more impactful on the likelihood of land development than market uncertainty.

The left censoring and left truncation are the caveats concerning the validity of the existing results. Extant studies commonly assume the initial year of the sample period as the year of land acquisition because of data limitations, and [Cunningham \(2006\)](#page-15-16) notes that this hypothetical beginning of exposure to development risk is problematic. The left censoring is the inclusion of land parcels with the unobservable actual onset of development risk before the sample period. An analysis that includes these parcels may also miss those lands that exposed to the risk during the same time but concluded with developments before the sample period. This second issue is the left truncation. [Cain et al. \(2011\)](#page-14-5) show that both the left censoring and truncation can substantially bias the estimates and severely underestimate the standard errors, and remedial methods yield unstable results when the fraction truncated is high.

The complete NTPU-D data of developers and their developable

lands are free of left censoring, left truncation, and right censoring and facilitate this research focusing on the waiting to build. The results from the Accelerated Failure Time (AFT) model suggest that developers with more paid-in capital or less development capacity tend to prolong the wait, but those who use a risk-shifting structure tend to shorten it, holding fixed important market conditions and land characteristics. The estimates have desired quality, suggested by a comparison with the counterfactual estimates obtained from a "pseudo sample" with the artificially created censoring and truncation, and by other robustness checks.

The findings regarding the heterogeneity of developers and uncertainty in project costs advance the real-option literature at the empirical front. Although there is an emerging interest to understand the roles of certain developer characteristics, the extant research is mainly theoretical (e.g., [Wang and Zhou, 2000](#page-15-20) [&2006](#page-15-7); [Shen and](#page-15-21) [Pretorius, 2013](#page-15-21); [Dong and Sing, 2017\)](#page-15-8). Our empirical research plausibly builds on renowned theories of the real option, and the results provide useful implications and also lend support to some of the newer theoretical works.

The paper proceeds as follows. [Section 2](#page-2-0) presents key background information on the NTPU-D study area and the workings of the land development and housing market. While the paper's contribution is not at the theoretical front, [Section 3](#page-2-1) lays out a conceptual modeling framework that can help readers to see the economics of the empirical findings in the context of the real option. [Section 4](#page-4-0) introduces the data work and draws reference from [Section 3](#page-2-1) to communicate the testable hypotheses and expected results. [Sections 5](#page-5-0) and [6](#page-5-1) present and discuss the empirical methodology and estimation results, respectively. [Section 7](#page-13-0) discusses the implications and makes the conclusions.

#### <span id="page-2-0"></span>**2. Background**

This research is on the National Taipei University District (NTPU-D). Mapped in Panel A of [Fig. 1,](#page-1-0) the district includes the Sanxia Main Campus of the National Taipei University (NTPU) and the surrounding area. Concerning the lack of a prestigious university in the populous Taipei County (now the New Taipei City) and the county's stagnant Sanxia Township, the central and county governments started the planning of NTPU in 1986 and opened the campus in 2000. Designated in 1990, NTPU-D was to meet the foreseeable residential and commercial land demand that grew with the development of the university. The government acquired all private land in the district through eminent domain and demolished all buildings by 1994. Land auctions started in 1999 and completed in 2007. Private developers acquired 79 out of the 80 parcels sold. As shown in Panel B of [Fig. 1](#page-1-0), most land sales happened between 2003 and 2006, whereas most land developments occurred before 2008 except for two parcels.[3](#page-2-2)

One unique difference between Western and Asian developers in the residential sector is that the latter often handle large-scale high-rise developments involving enormous investment in land acquisition, building construction, and advertisement before project completion given a high-density urban environment and more restrictive capital market. Thus, presale – a legal framework permitting sales of properties before the project completion but after the issuance of construction permits – is common in Asia.[4](#page-2-3)

Taiwanese developers' practice of presales started in 1969, with the growing housing demand of baby boomers and difficulty to obtain construction loans to finance projects at that time. [Chan et al. \(2008](#page-14-6); [2014\)](#page-14-7) argue that developers and buyers can both benefit from the presale system by reducing financial costs when builders have limited accessibility to the capital market. The presale also carries other benefits. It reflects the reputation of developers in forward price ([Chau et al., 2007](#page-15-22)), decreases inventory costs ([Lai et al., 2004\)](#page-15-23), and reduces the entry barrier for new developers [\(Chiang et al., 2004\)](#page-15-24). The presale thus remains the primary channel of sales in Taiwan although the capital market has become mature and accessible.

Property development in Taiwan also features some institutions, which are worth discussion. First, developers need not bear any carrying cost when they hold vacant land and leave it undeveloped; there is no tax on vacant land and no restriction on the maximum holding period. Thus, no institutional constraints affect time to development. Second, establishing a project-specific subsidiary for risk-shifting is common in Taiwan. For example, 47% of developers in our sample launched projects in NTPU-D using subsidiaries, and 37% of these subsidiaries only completed one single project and then closed down. The presale practice helps project financing and eases startups of small subsidiaries. Developers, therefore, consider a project-specific subsidiary a protection of their finance and reputation from project financial and default risks and against disputes arose from asymmetric information in the presale market [\(Chau et al., 2007;](#page-15-22) [Leung et al.,](#page-15-25) [2007\)](#page-15-25).

#### <span id="page-2-1"></span>**3. Theoretical framework**

This section sets out a theoretical framework, with the objectives of validating the specification of regression models and convincing the interpretation of empirical results in subsequent sections. The framework is a derivative of several renowned articles, including [McDonald and Siegel \(1986\)](#page-15-5), [Capozza and Helsley \(1990\)](#page-14-2), and [Bulan et al., \(2009\).](#page-14-4) Because the purpose is to highlight our paper's empirical contributions but not about adding an extension of the wellestablished real-option theory, we choose not to present the full model and its complete solutions for succinctness, but to introduce the essential elements and discuss their deliverable results within this conceptual framework of the timing to build.

#### *3.1. Uncertainty and irreversibility capture the essence of waiting*

A vacant parcel of a developer is an option of land development. [McDonald and Siegel \(1986\)](#page-15-5) show why profit-maximizing developers often defer the projects and leave lands vacant. The *irreversibility* of land development and the *uncertainty* of future cash flows and development costs together explain the result, which can hold even if the shareholders are risk-neutral rather than risk-averse.

The essentials of their theory are the stochastic processes of the project value and costs. The developer can pay development costs *Ft* to launch the project at any time *t* ≥ 0 and expect a sequence of future net cash flows whose present value is *Vt* since then. By assumption, both *Ft* and *Vt* follow geometric Brownian motion (GBM):

$$\frac{dV}{V} = \alpha\_{\psi} dt + \sigma\_{\psi} d\mathfrak{z}\_{\psi}$$

and

$$\frac{dF}{F} = \alpha\_f dt + \sigma\_f d\mathbf{z}\_f$$

where *αv* and *αf* are the expected growth rates of the present value and development costs, respectively, and *σv* and *σf* are the corresponding standard deviations, which are amplified by a standard Wiener process of *zv* or *zf* over time.

The GBM carries nice properties that make the real-option theory straightforward and intuitive. Particularly, the stochastic variable, say *Vt*, at any time *t* is a log-normally distributed random variable and its expected value *E(Vt)* increases in time. As a result, the expected waiting

<span id="page-2-2"></span><sup>3</sup> Auctions of 7 parcels occurred in 1999 prior to completion of the infrastructure of NTPU-D in 2000. Given impossibility of project development at this stage, we consider these 7 parcels as pre-auctions and adjust their acquisition dates to the time of infrastructure completion.

<span id="page-2-3"></span><sup>4</sup> Nevertheless, the presale system has gradually gained attention in certain cities in the U.S. and Canada ([Chan et al., 2008](#page-14-6)).

time for *Vt* to hit an arbitrary positive number *c*¯ for the first time is simply *c*¯*/αv*. Also, the quotient of two GBM processes, say *Vt/Ft*, still follows GBM[.5](#page-3-0)

The developer decides a boundary {*C* <sup>=</sup> \*} *t tT* <sup>0</sup> such that the project launches on the first occasion that *V F C* / > \* *t t <sup>t</sup>* . The boundary is a constant *C*\* at all times when the time horizon is ∞, and it defines the decision rule that maximizes the present value of the expected payoff *E V F e* [( ) ] *t t µt* <sup>0</sup> at *t = 0* and given the discount rate *μ*. A well-defined solution requires *αv<μ*; the expected growth rate of the periodic cash flow must be smaller than the discount rate.

The option value of the vacant land, *P*\* *<sup>O</sup>*, is the maximum of the above optimization problem of the developer[.6](#page-3-1) A higher option value implies a longer expected waiting time before the project launch. [McDonald and Siegel \(1986\)](#page-15-5) demonstrate that *greater uncertainty* arising from a larger variance of *Vt/Ft* (i.e., *σ2* in Footnote 1) will raise the option value. The uncertainty about *Vt/Ft* can intensify, with (i) a larger variance of *Vt* relating to the project value, (ii) a bigger variance of *Ft* on the development costs, or (iii) a smaller instantaneous correlation between *Vt* and *Ft*'s rates of change. The option value is also an increasing function of *αv* and a decreasing function of *αf* and *μ*.

#### *3.2. Connection with the conditional probability of time to development*

The translation of the developer's profit-maximizing decision into the conditional probability of the project launch at time *t* is simple since the expected waiting time closely and positively relates to the optimal boundary condition *C\**. Given a boundary value prescribed for a Brownian motion, there exists a first hitting time, which is the first time the value of the stochastic process reaches the boundary. The connection of the theoretical first hitting time to the empirical proportionalhazard and accelerated-failure-time models are well received (e.g., [Lee and Whitmore, 2006](#page-15-26)). An example is in [Bulan et al., \(2009\)](#page-14-4). In the context of our paper, the conditional probability is:

$$h(t) = \pi \left(\frac{V\_t}{F\_l} \ge \mathcal{C}^\* | \frac{V\_{t'}}{F\_{l'}} < \mathcal{C}^\*, \,\forall \, t' < t\right).$$

A higher boundary *C\** implies a lower hazard rate to launch the project at time t.

#### *3.3. Spatial variation in the option value and waiting*

Locations may influence the option value. [Capozza and](#page-14-2) [Helsley \(1990\)](#page-14-2) integrate a Brownian motion into a monocentric city surrounded by undeveloped rural land, while they argue that the more common GBM assumption can also work.[7](#page-3-2) They assume the project value is stochastic, but the development cost is constant.

Specifically, households commute to the city center (CBD) to earn income *y(t)*, and a round-trip costs *τ* per unit of distance. Each household inelastically demands one unit of land, pays the commuting cost given the residential location, and spends the rest of the income consuming the numeraire, which generates the utility. The necessary equilibrium condition of spatial indifference can derive a downward sloping bid-rent curve and pin down each urban location's periodic rent *R(t,z)*, in which the second argument indicates the distance to CBD. For simplicity, we can add one more assumption than [Capozza and](#page-14-2) [Helsley \(1990\)](#page-14-2) that rural land is non-agricultural and generates no cash flow.

[Capozza and Helsley \(1990\)](#page-14-2) assume that household income follows Brownian motion; *y t*( ) = +*t* B( )*t vh vh* . The expected growth rate of the household income is *αvh*, and the development cost is *F*. Thus, rural parcels will become urban land in the future. If *σvh = 0*, income growth is deterministic. Τhe periodic urban rent is *R t s z* ( , ; ) ( + = *z t z* \* ( ) ) + +*s µF z z t t s* , < \* ( ), , *vh vh* , where *z*\*(*t*) is the city edge at time *t*. The first term is the location premium from saving commuting cost, the second is a growth premium, and the third is the cost of financing the development at the discount rate *μ*. Consequently, the urban land price is *P t z* ( , ; ) ( ( = *z t z F z z t t* \* ( ) ) ) , + + < \* ( ), *<sup>L</sup> <sup>u</sup> vh <sup>µ</sup> <sup>µ</sup>* <sup>1</sup> *vh* , which comprises the present value of the periodic rent and development cost. At the city edge *z*\*(*t*), the differential between urban and rural land prices is simply the development cost.

Rural lands currently have no use, but their prices are strictly positive because the developer will convert them into urban use at some point and generate rents afterward. The rural land price is *P t z* ( , ; ) ( = *e* ), *z z t t* > \* ( ), *<sup>L</sup> <sup>r</sup> vh <sup>µ</sup> <sup>µ</sup>* <sup>1</sup> *vh* (*z z t* \* ( )) *<sup>µ</sup> vh* , in which by geometry, (*z z t* \* ( )) *vh* is equivalent to the time to development *t z t* \* ( ) at the given *z* and *t*. The price of rural land is a decreasing function in the distance to the urban fringe because land development is gradually toward the outskirt. The development of a rural parcel that is further away is in the more distant future, and the conversion of the periodic rents, which are derivable after the development, to the present value is subject to more discount.

When *σvh> 0* and income is stochastic, the developer solves the profit-maximizing boundary *R\** and infers the first hitting time *t\*(z)*, which we discussed earlier. [Capozza and Helsley \(1990\)](#page-14-2) demonstrate that the uncertainty of renters' income generates additional values, which they term irreversibility premium, for lands not only in rural areas but also in urban locations.

To see the economics of this finding, note that the developer now needs the positive differential between *R\** the boundary and *μF* the opportunity cost of development capital to compensate for the uncertainty. This "compensating differential" increases in *σvh* but decreases in *αvh*, as the standard real-option theory. A larger differential translates to a longer expected wait.

For developed urban land, the compensating differential constantly exists in periodic rents. Thus, the present value of these added differentials is (*R µF µ z z t t* \* )/ , < \* ( ), . This amount is the irreversibility premium added to the urban land price when there exists the uncertainty (i.e., (*R µF µ P t z* \* )/ ( , ; , ) ( , ; ), = *<sup>L</sup> P t z z* < *<sup>u</sup> vh vh <sup>L</sup> <sup>u</sup> vh z t t* \* ( ), .

For undeveloped rural land, the irreversibility premium also adds to the price to an extent. The rural land price becomes *P t z* ( , ; , ) ( = + *R µF e* \* ) , *z z t t* > \* ( ), *<sup>L</sup> <sup>r</sup> vh vh <sup>µ</sup> <sup>µ</sup> z z t* 1 *vh* ( \* ( )) . Note that *δ* replaces *μ/αvh* used in the deterministic case and *δ* ≤ *μ/αvh* because *σvh* influences the moment generating function for *t\*(z)*.

In summary, [Capozza and Helsley \(1990\)](#page-14-2) confirm that uncertainty can prolong the wait and generate option values for lands. On the new insights, they find these premiums contribute to not only undeveloped parcels but also developed lands. A longer wait is expectable for a vacant parcel that is further away from CBD in theory, but whether that additional wait is empirically significant also depends on other factors such as the variable cost of commuting and the urban structure.

#### *3.3. A gap in development costs*

Extant studies have commonly left out *Ft*, the development costs, or assume it to be a constant in the vast majority of the literature, including [Bulan et al., \(2009\)](#page-14-4), who point out that data on development costs are difficult to obtain. Indeed, looking into the microdata of individual developers is a necessary step to make the theoretical

<span id="page-3-0"></span><sup>5</sup> By Ito's lemma, = ( + )*dt* + *dz dz dV F V F v f <sup>f</sup> vf v f v v f f* / / <sup>2</sup> , where *ρvf* is the instantaneous correlation between the rates of changes of *V* and *F*.

<span id="page-3-1"></span><sup>6</sup> The option value is *P C F <sup>O</sup>* \* = ( \* 1) ( ) *V F <sup>C</sup>* <sup>0</sup> <sup>0</sup> / <sup>0</sup> \* where *C*\* = /(1 ) and <sup>=</sup> (( ) ) ( ) + + *av af µ af av af* 2 1 2 <sup>2</sup> 2( ) <sup>2</sup> 0.5 <sup>1</sup> <sup>2</sup> <sup>2</sup> such that = +*v f* <sup>2</sup> *vf v f* <sup>2</sup> 2 2 is the variance of *V/F* where *ρvf* is the instantaneous correlation between the rates of changes of *V* and *F*.

<span id="page-3-2"></span><sup>7</sup> From a modeling view point, the deviation from the common GBM assumption allows the variable cost of commuting to be monetary so that adding a household's time constraint is unnecessary.

development of *Ft* meaningful and is a considerable value add to the empirical literature.

# <span id="page-4-0"></span>**4. Data and hypotheses**

The research concerns the time to develop, which is the period of waiting between land acquisition and development. The data work merges information from various sources. We access results of all the land auctions won by private developers through the Land Administration Department of the New Taipei City Government and obtain complete information of those land parcels' construction permits through the government's Building Management Information System. The first source records useful information, including the transacted price, location, and date of sale. The second source verifies the date the construction began and who the developer was. The Land Registry assigns each parcel an ID that facilitates data merging to compute accurate waiting time to develop. We also obtain developers' information from the Ministry of Economic Affairs (MEA) and their past projects from *My Housing Quarterly*. We collect the construction permits of all these historical projects to generate useful information for analysis.

The compiled sample includes a total number of 515 quarterly observations between the years 2000 and 2011 and consists of timevarying information regarding the NTPU-D's 79 parcels acquired by 35 developers.[8](#page-4-1) [Table 1](#page-5-2) lists all variables' names, abbreviations, and definitions.

The data have two major advantages. First, lands in NTPU-D are homogeneous, because of the way the city government planned this development zone through the eminent domain. This greatly eases a concern that unobservable heterogeneity of lands might correlate with the characteristics of developers who acquire the parcels in later analyses.

Second, our sample does not have any left censoring, left truncation, and right censoring.[9](#page-4-2) Unlike this research, the existing studies encounter those issues, and their incomplete data challenge the identification. The literature of survival analysis points out: The censoring and truncation can bias estimates and severely underestimate standard errors when the loss of information is significant [\(Leung et al., 1997](#page-15-27); [Cain et al., 2011](#page-14-5)). The utmost underestimation is the percentage of censored observations [\(Lagakos, 1979\)](#page-15-28).

With the data, the research can test three hypotheses on relationships between developers' characteristics and timing to build. The rationales relate to the expectation and uncertainty about the development costs and come from the real-option framework in the theory section.

First, developers with more *Paid-in Capital*(*PC*) tend to wait longer. A preferable proxy of the firm size, the paid-in capital is the total amount of money that the owners or shareholders have put into funding the company. It is the capital for day-to-day operations. It is also decisive to the credit line and interest rate for borrowings, especially the vast majority of the developers, including those in the sample, are not publically listed. Developers with ample paid-in capital could expect easier credits translating to a lower drift *αf* of the development costs. As a result, the option value is higher, and the expected wait is longer.

Second, developers who presently have more *Development Capacity* (*DC*) tend to shorten the wait. This quarterly variable is *minus one* times the aggregate gross floor area of the developer's projects in the presale market relative to its paid-in capital.[10](#page-4-3) The numerator indicates the aggregate scale of all ongoing projects, and the denominator is a proxy of firm size. Note the negative sign. The bigger this variable, the less the developer stretches in managing unexpectable occasions demanding adhoc temporary workers. A developer with larger development capacity would perceive a smaller variance *f* <sup>2</sup> of project costs for the vacant land and tend to shorten the wait.

Third, developers tend to shorten the wait if they ever practiced *Subsidiarization*(*SUB*), which is to establish a subsidiary to launch a project in NTPU-D.[11](#page-4-4) The literature has acknowledged subsidiarization to be a measure of risk-shifting (e.g., [Kahn and Winton, 2004](#page-15-29); [Dell'Ariccia and Marquez, 2010\)](#page-15-30), because it is a diversification strategy for firms to shield from large losses. Shifting the risk and isolating it within the subsidiary can reduce the variance of costs, lower the option value, and shorten the expected wait.

Relevant macro-environmental factors and land features are also included as the controls.[12](#page-4-5) We measure the *District's Maturity* (*DM*) using the length of time from the district's infrastructure-completion date to the land's acquisition date. The literature acknowledges that the maturity of the built environment may affect the price premium of land development [\(Ogu and Ogbuozobe, 2001](#page-15-31); [Wu et al., 2015](#page-15-32); [Turok, 2016](#page-15-33)). The growth of a district could gradually involve many external or internal factors, but the project launch is irreversible. At the infrastructure-completion date, the raw land became developable but the whole district was still empty; there was much uncertainty (i.e., a large *<sup>v</sup>* 2 ) about the value a project can bring. Thus, a developer who acquired a parcel nearer to the infrastructure-completion date is more likely to extend the wait for that land. On the other hand, a developer who acquired a parcel at a later time when the district became more mature can expect a smaller variance in the project value, because the success of the zone is more certain and it can plan a project that eventually better fits the local economy. The expected wait would be less.

*Competition* (*COMS*) in the market is another macro-environmental factor. The real-option theory suggests that the prices of earlier developments may constraint the pricing of subsequent projects. Greater potential competition implies a lower drift *αv* of the project value. Thus, developers may shorten the expected wait if the potential competition is stiff [\(McDonald and Siegel, 1986;](#page-15-5) [Grenadier, 1996\)](#page-15-34). We define the degree of the competition as the total size of all other undeveloped parcels of NTPU-D held by the developers in the current quarter.

<span id="page-4-1"></span><sup>8</sup> [Appendix A](#page-14-8) reports the distribution regarding number of parcels held by developers. In general, the 79 land parcels in NTPU-D are fairly distributed to different developers. The average number of parcels held by per developer is 2.26.

<span id="page-4-2"></span><sup>9</sup> On the waiting to build, the start and end of the risk exposure happen on the acquisition date and at the project launch, respectively. The left censoring presents if the sample has a parcel acquired before the sample period so that the exact time that the subject has exposed to the risk is unknown. The left truncation happens when a land exposes to the risk at the same time as the censored subject but is unobservable because its development is before the sample period. Lastly, the right censoring occurs when a parcel is observable, but its project begins after the period.

<span id="page-4-3"></span><sup>10</sup> The variable only considers projects in the Taipei metropolitan area, which includes both the Taipei City and New Taipei City. This is the greater economic area to which NTPU-D belongs. The international and local literature finds that the great majority of developers focus on their local or regional markets because real estate markets are highly heterogeneous, despite the top players have gradually globalized. Most developers in Taiwan mainly focus on one or two cities. Also, the presale is the predominant form of new housing sales in Taiwan. By law, obtaining the construction permit, which means the project launch, is necessary for starting the presale, and the groundbreaking must happen within six months after receiving it. Thus, we use the projects in presales to measure the ongoing projects.

<span id="page-4-4"></span><sup>11</sup> We search business registry records of MEA and match the owners or addresses to identify whether a developer has subsidiaries to launch projects in the district.

<span id="page-4-5"></span><sup>12</sup> Our primary observables exclude the market uncertainty, which the readers might be interested, because it is hard to measure ([Somerville, 2001;](#page-15-35) [Cunningham, 2006](#page-15-16); [Miles, 2009\)](#page-15-36) and its standard acceptable proxy, i.e., the variance of local housing prices, is inapplicable and undefined in our case; the NTPU-D was a new district with no prior transactions. The variance of nearby areas' prices cannot proxy the NTPU-D's market uncertainty, because properties in those old areas belong to a different market as the built environment greatly differs from the modern NTPU-D.

<span id="page-5-2"></span>**Table 1**

Variable definitions.

| Variable                                         | Abbreviation | Definition                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auction price                                    | AP           | Auctioned unit price (UP) times the size of project (SIZE).                                                                                                                                                                                                                                                                          |
| Competition(Number)                              | COMN         | Total number of all other undeveloped land parcels held by the developers in NTPU-D in the current quarter.                                                                                                                                                                                                                          |
| Competition(Size)                                | COMS         | Total size of all other undeveloped land parcels held by the developers in NTPU-D in the current quarter.                                                                                                                                                                                                                            |
| Development capacity                             | DC           | Minus one times the aggregate gross floor area of the developer's projects in the presale market in the current quarter<br>relative to the paid-in capital. The variable only considers projects in the Taipei metropolitan area, which includes<br>both the Taipei City and New Taipei City.                                        |
| Distance to market center                        | DTMC         | Straight-line distance from the parcel to the hypermarket Carrefour located in NTPU-D.                                                                                                                                                                                                                                               |
| District's maturity                              | DM           | The length of time from the district's infrastructure-completion date to the land's acquisition date.                                                                                                                                                                                                                                |
| Outskirt                                         | OS           | Dummy variable that equals one if the land is at one of the perimeter roads along the district boundary and zero<br>otherwise.                                                                                                                                                                                                       |
| Paid-in capital                                  | PC           | Amount of fund the company raises through the primary market. Paid-in capital is registered in the ministry of<br>economic affairs, R.O.C.                                                                                                                                                                                           |
| Subsidiarization                                 | SUB          | Dummy variable that equals one when developer ever established a subsidiary to launch a development in NTPU-D<br>and zero otherwise. We search business registry records of MEA and match owner or address information of<br>developers to identify whether a developer has subsidiaries in development of projects in the district. |
| Time to development (i.e., the survival<br>time) | T            | The time of waiting, measured in quarters, since the land acquisition.                                                                                                                                                                                                                                                               |

Following the literature [\(Bulan et al., 2009;](#page-14-4) [Wang et al., 2016](#page-15-19)), we also use the total number of all other undeveloped parcels (*COMN*) as an alternative measure of competition for robustness.

On the characteristics of the parcels, the *Auction Price* (*AP*), which depends on the unit price and land size, may relate to the carrying costs. In theory, the higher the value, the shorter the expected wait the developer would bear ([Williams, 1991](#page-15-6)). In practice, the significance of this variable is an open question, because the carrying cost of vacant lands in Taiwanese land markets is generally low.

The land quality is rather homogeneous due to NTPU-D's development process, as explained earlier. The mere heterogeneity is the location that is characterizable by two variables. One is *Distance to Market Center*(*DTMC*), the straight-line distance from the parcel to the hypermarket Carrefour, which marks the center of the district's only commercial zone. The other is the *Outskirt* (*OS*), which indicates whether the land is at one of the perimeter roads along the district boundary.[13](#page-5-3) Land plots at the perimeter roads are not only further away from the center but also adjacent to neighborhoods with a more rundown build environment. The parcels further away from the center are subject to longer expected wait, a theoretical prediction of [Capozza and](#page-14-2) [Helsley \(1990\)](#page-14-2) elaborated in the theory section. However, the empirical significance of the two variables also depends on the variable cost of commuting and the urban structure. More discussion is in the result section.

### <span id="page-5-0"></span>**5. Empirical methodology**

Our baseline regression adopts the Accelerated Failure Time (AFT) model bellow:

$$\ln(T\_{\overline{\rm{ly}}}) = \beta\_0 + \beta\_1 PC\_{\overline{\rm{ly}}} + \beta\_2 DC\_{\overline{\rm{ly}}} + \beta\_3 SUB\_{\overline{\rm{ly}}} + \beta\_4 DM\_l + \beta\_5 COMS\_{\overline{\rm{ly}}} + \beta\_6 AP\_l$$

$$+ \beta\_7 DTMC\_l + \beta\_8 OS\_l + \gamma\_{\overline{\rm{ly}}} + \varepsilon\_{\overline{\rm{ly}}},\tag{1}$$

where *Tijt* denotes the total number of quarters that parcel *i* had been kept vacant by developer *j* since the land acquisition till the present quarter *t*. It is the survival time recorded by the observation. The variables *PCij, DCijt*, and *SUBij* are developer-specific characteristics, and *DMi, COMSit, APi, DTMCi*, and *OSi* are the macro-environmental factors and location characteristics. The term *γj* is the shared frailty, which follows a Gamma distribution. The frailty captures the unobserved developer-specific heterogeneity, a latent perspective of failure risk commonly shared by the developer's parcels.[14](#page-5-4) The time-varying covariates, which have *t* in the subscript, are permissible by the method of [Cox and Oakes \(1984\)](#page-15-37). The logarithmic transformation applies to all the continuous variables.

The AFT model is parametric. It is a popular alternative to the semiparametric Proportional Hazard (PH) method for survival analysis.[15](#page-5-5) It is more suitable for this research because it works better for small samples than the PH. The literature (e.g., [Efron, 1977;](#page-15-38) [Oakes, 1977](#page-15-39); [Cox and Oakes, 1984](#page-15-37)) cautions against the poor asymptotic efficiency of the PH in handling samples that are small (or have notable censoring); the efficiency worsens when estimates are further away from zero.

Also, the AFT allows a flexible error-term distribution. The lognormal distribution is chosen, given its empirical applicability. It also allows a translation of the covariate's effect on the failure time into the time ratio, making the result interpretation straightforward.

The shared frailty [\(Lambert et al., 2004\)](#page-15-40) can handle unobserved heterogeneity. It is an extension of the frailty method [\(Gutierrez, 2002\)](#page-15-41) for univariate survival data. It is useful when the unobserved risk of failure is the same within each group of subjects but different across the groups. Since lands are homogeneous but developers have unobservable differences, a shared-frailty specification on developer heterogeneity can serve well in this research.

With the complete information of all land acquisitions and project launches, the research on the NTPU-D can take advantage of the precise entry and exit of exposure to land-development opportunity, and the estimation of the AFT can analyze the influencing factors on timing to build.

#### <span id="page-5-1"></span>**6. Estimation results**

#### *6.1. Summary statistics*

[Table 2](#page-6-0) reports the summary statistics. The time to development is *Tijt*. For each observation, it is the survival time, the time the developer has waited since the land acquisition. Its mean and median are equal to 854 and 511 days, respectively. [Fig. 2](#page-7-0) exhibits the observed cumulative distribution function of the time to develop. Half of the projects launched within one and a half years after land acquisitions. Beyond that, the wait prolonged, although 80% of the projects started within four

<span id="page-5-3"></span><sup>13</sup> The perimeter roads include Fuxing, Guoqing, Jiayuan, Sanshu, Xuecheng, and Xuefu Roads.

<span id="page-5-4"></span><sup>14</sup> Instead of using the Gamma distribution, which assumes relatively constant

<sup>(</sup>*footnote continued)*

variability among developers, the regressions in [Appendix B](#page-14-9) adopts the inverse Gaussian distribution for the shared frailty and affirms robustness of the results.

<span id="page-5-5"></span><sup>15</sup> Compared with AFT, PH concerns the failure rate of the event instead of the time scale of the failure. Nevertheless, the two types of models closely relate to each other because a higher (lower) failure rate implies a shorter (longer) failure time.

#### <span id="page-6-0"></span>Summary statistics

Panel A reports the summary statistics of 515 observations from 2000 to 2011. In Panels B and C, Columns (1), (2) and (3) report the mean of the first, second and third terciles divided according to the acquisition date and development date, respectively. Each tercile consists of one-third of the 79 land parcels. The fourth column reports the mean difference between the first and third terciles. The asterisk marks \*\*\*, \*\* and \* indicate 1%, 5% and 10% levels of significance, respectively.

| Panel A: Summary |                         |         |         |            |        |            |  |
|------------------|-------------------------|---------|---------|------------|--------|------------|--|
| statistics       | Measurement             | Mean    | Median  | StD.       | Min.   | Max.       |  |
|                  | units                   |         |         |            |        |            |  |
| PC               | \$ (million)            | 2292.38 | 125.00  | 3937.12    | 1.00   | 18,500.00  |  |
| DC               | m2 /                    | -0.16   | -0.02   | 0.68       | -8.69  | -0.01      |  |
|                  | PC × 1000               |         |         |            |        |            |  |
| SUB              | 1: yes; 0: no           | 0.47    | 0.00    | 0.50       | 0.00   | 1.00       |  |
| DM               | day                     | 1089.34 | 1275.00 | 733.35     | 0.00   | 2150.00    |  |
| COMN             | parcel                  | 16.93   | 17.00   | 9.61       | 0.00   | 36.00      |  |
| COMS             | m2 (thousand)           | 65.21   | 66.35   | 41.34      | 0.00   | 141.32     |  |
| T                | day                     | 853.69  | 511.00  | 644.00     | 74.00  | 2079.00    |  |
| AP               | \$ (million)            | 284.42  | 167.74  | 415.90     | 28.92  | 5120.17    |  |
| UP               | \$ (thousand)           | 53.65   | 51.60   | 9.02       | 42.60  | 74.00      |  |
| SIZE             | m2                      | 4907.40 | 3129.57 | 7167.57    | 600.00 | 100,003.39 |  |
| DTMC             | m                       | 478.00  | 461.38  | 253.56     | 1.00   | 1068.11    |  |
| OS               | 1: yes; 0: no           | 0.28    | 0.00    | 0.45       | 0.00   | 1.00       |  |
|                  | Panel B: Variable means |         |         |            |        |            |  |
|                  | by the order of the     |         |         |            |        |            |  |
|                  | land acquisitions       |         |         |            |        |            |  |
|                  | (1)                     | (2)     | (3)     | (3) - (1)  |        |            |  |
| PC               | 3040.76                 | 1331.30 | 2263.96 | -776.80    |        |            |  |
| DC               | -0.07                   | -0.14   | -0.13   | -0.06      |        |            |  |
| SUB              | 0.56                    | 0.73    | 0.46    | -0.10      |        |            |  |
| DM               | 682.68                  | 1451.87 | 1753.04 | 1070.36⁎⁎⁎ |        |            |  |
| COMN             | 16.12                   | 22.30   | 25.42   | 9.30⁎⁎⁎    |        |            |  |
| COMS             | 40.73                   | 86.49   | 98.14   | 57.41⁎⁎⁎   |        |            |  |
| T                | 720.68                  | 304.4   | 522.75  | -197.90    |        |            |  |
| AP               | 238.89                  | 355.16  | 402.95  | 164.06*    |        |            |  |
| DTMC             | 685.98                  | 409.47  | 347.03  | -338.94⁎⁎⁎ |        |            |  |
| OS               | 0.24                    | 0.23    | 0.38    | 0.14       |        |            |  |
|                  | Panel C: Variable means |         |         |            |        |            |  |
|                  | by the order of the     |         |         |            |        |            |  |
|                  | land development        |         |         |            |        |            |  |
| PC               | 2188.58                 | 1466.15 | 2838.62 | 650.04     |        |            |  |
| DC               | -0.07                   | -0.11   | -0.16   | -0.09⁎⁎    |        |            |  |
| SUB              | 0.58                    | 0.70    | 0.50    | -0.08      |        |            |  |
| DM               | 874.81                  | 1313.11 | 1711.42 | 836.62⁎⁎⁎  |        |            |  |
| COMN             | 12.84                   | 23.07   | 27.88   | 15.04⁎⁎⁎   |        |            |  |
| COMS             | 56.59                   | 79.97   | 89.93   | 33.34⁎⁎⁎   |        |            |  |
| T                | 436.62                  | 492.07  | 579.12  | 142.50     |        |            |  |
| AP               | 194.29                  | 411.22  | 390.12  | 195.83⁎⁎   |        |            |  |
| DTMC             | 637.37                  | 440.79  | 357.28  | -280.09⁎⁎⁎ |        |            |  |
| OS               | 0.15                    | 0.22    | 0.46    | 0.31⁎⁎     |        |            |  |
|                  |                         |         |         |            |        |            |  |

years. The longest wait extended 2,079 days, about 28 times of the shortest. The variation in development timing is non-trivial.

Panel A of [Fig. 3](#page-8-0) compares the observed probability density function of the logarithmic time to development with its best fitted lognormal distribution. The logarithmic survival time follows a normal distribution well especially at the left tail and the middle range, although there are small additional modes leading to some deviation at the right tail.

Panel B plots the observed probability density function of the wait and its best fitted exponential and Weibull distributions, which are two other popular assumptions. The exponential distribution is clearly not a good fit. The Weibull distribution captures the hump shape but shows large deviations throughout the support. Generally, the permissible distributional assumptions of AFT are incompatible with multiple modes. We choose the logarithmic distribution, which appears less sensitive to the additional modes, as the preferred assumption of the error term.

On developer characteristics, the paid-in capital (*PC*) is worth mention. Its mean and median before the logarithmic transformation are 2,292 and 125 million, respectively. While large developers ventured into NTPU-D, many small players also participated. The dispersed distribution was partly due to the institution allowing developers to establish a subsidiary to handle a single project and finance that project through the presale. The institution provided a channel to diversify risk, and 47% of the developers were in association with subsidiaries (*SUB*).

We also categorize the parcels into terciles by the date of acquisition or development and calculate the corresponding mean to provide additional descriptive information. In Panels B and C of [Table 2](#page-6-0), the first three columns list out the mean of each tercile, and the last column notes the mean difference between the first and the third. Developers with more development capacity (DC) seemed to venture into the market earlier and be front-runners in development. Large developers (*PC*) seemed to enter earlier but launch later, while those who establish subsidiaries *(SUB)* appeared to enter earlier and start earlier. The difference is insignificant in these two aspects. In terms of market conditions, the lands acquired or developed later naturally were in an environment with greater district's maturity (*DM*) and more competition (*COMS*). The lands auctioned earlier tended to be cheaper (*AP*). The land sales and developments seemed to have an ambiguous geographic patterns. These stylized facts warrant more rigorous tests on the time to development.

[Table 3](#page-9-0) reports the correlation coefficients and the variance inflation factor (VIF) for each explanatory variable. Multicollinearity is not a concern since all VIF values are less than four. Many pairs of variables, nevertheless, do have some correlation, mild but significant. Interestingly, the correlation patterns support connecting subsidiarization with risk shifting as the literature does. Large developers with more paid-in capital (*PC*) positively relate to subsidiarization (*SUB*). Also, subsidiarization positively relates to the district's maturity (DM).

#### *6.2. Effects of developers' perspectives on time to development*

The survival-time analysis concerns the deterministic characteristics of the wait to build. For the AFT estimation, all tables report the time ratio, which is the exponentiated coefficient *e β* , and its corresponding standard errors. The time ratio is a factor multiplying the expected time to failure due to a unit increment of the covariate, making the result interpretation intuitive.

In [Table 4,](#page-9-1) Column (1) includes the market conditions and land characteristics but excludes the developer characteristics. The result is sensible and in line with the earlier discussion. When *DM* the district maturity, which is the time from the infrastructure-completion date to the land-acquisition date, increases 1%, the expected wait significantly shorten by around 0.14%. When *COMS* the potential competition from other development opportunities intensifies by 1% more, the expected delay significantly reduces by about 0.26%.

Notably, the estimates of *AP, DTMC*, and *OS* are all insignificant. This feature continually presents in all other AFT specifications. This result is not a disagreement with [Capozza and Helsley \(1990\)](#page-14-2) for two apparent reasons. The NTPU-D is a new development zone with good road infrastructure and planning. The commuting cost per unit of distance is modest, and the district itself is not large. Also, the commercial area centered at the hypermarket Carrefour is not a dominant core for economic activities. A clear monocentric structure is absent. In fact, the insignificant estimates of these variables lend support to our argument about homogenous land. If there was any critical unobserved heterogeneity that correlates with locations or prices, the estimates of these three variables will absorb the influence and show significance.

Developer characteristics are the key variables in [Table 4.](#page-9-1) Step by step, Columns (2) to (7) include the three variables regarding developers' perspectives on the timing to build. The even columns do not have the shared frailty, but the odd columns include it to add robustness. The estimates are invulnerable to unobserved developer heterogeneity because they are insensitive to the inclusion. Especially, the results of Columns (6) and (7) are almost identical. Not having shared

<span id="page-7-0"></span>**Fig. 2.** Cumulative distribution function of time to development

This figure shows the cumulative distribution function of time to development and the time. Time to development is the period of waiting between the land acquisition and development.

#### frailty is harmless.

Column (7) has the most comprehensive specification and provides the baseline result. The three developer characteristics all have significant effects on the expected waiting time, albeit a weaker level of significance for the *PC* (paid-in capital). A 1% increase in *PC* leads to an approximately 0.05% longer time to develop. A 1% increase in *DC* (development capacity) shortens the wait by about 0.06%. Developers involved in SUB (subsidiarization) for risk-shifting tend to expedite land development; the delay is 29.6% shorter. The results are consistent with our hypotheses developed from the theory in [Section 3](#page-2-1). A larger PC may reduce *αf* and extend the expected wait, whereas a bigger *DC* or *SUB* can lower *σf* and shorten the wait.

#### *6.3. Robustness tests, institutional settings, and heterogeneous effects*

Developer characteristics significantly impact the time to develop; results show thus far. Additional robustness checks are in [Table 5](#page-10-0). Columns (1) and (2) adopt alternative measures of competition and market uncertainty, respectively. Columns (3) through (5) apply robust and bootstrapped standard errors. Columns (6) and (7) use OLS to compare having vs. not having time-varying covariates.

# *6.3.1. Alternative measures of competition and uncertainty*

Potential competition arises from other vacant lands held by the developers in NTPU-D. The analysis so far measures the competition using the aggregate size of those lands in the current quarter. Here, a robustness check follows [Bulan et al., \(2009\)](#page-14-4) and uses the total number of those lands (*COMN*) as an alternative measure, because one might think that the total number better reflects the likelihood that a developer's pricing ability may be constrained. The basic results, however, are insensitive to the use of this alternative measure, as shown in Column (1). A 1% increase in *COMN* shortens the expected wait by 0.36%, while a 1% change in *COMS* reduces it by 0.26%. More importantly, the positive impact of the paid-in capital becomes more significant, and the specification returns a better fit. The degree of competition might relate more to the number of rivals in the market, but the basic results are similar no matter we use the size or the number to measure competition.

As mentioned, the standard measure of market uncertainty is not well defined because old buildings were demolished en bloc in the NTPU-D. The district lacked residential properties and transactions in the early part of our study period. Although our take is that the modern NTPU-D and the surrounding old districts belong to different markets, one might wish to consider an assumption. The price movement in the adjacent market could have a ripple of the dynamic that passes to the district of interest ([Liao et al., 2015\)](#page-15-42); the volatility of housing prices in the adjacent market could serve as a proxy. Thus, we estimate the variance of the housing price index of the New Taipei City, which the NTPU-D belongs. Carried out through a GARCH (1, 1) model as in [Bulan et al., \(2009\),](#page-14-4) the estimated variance measures the market uncertainty of NTPU-D. Column (2) of [Table 5](#page-10-0) reports the results. The magnitude and significance of the effects of the developer characteristics have minimal change. The estimated impact of the market uncertainty is a longer time to development and is consistent with the literature, but this estimate is insignificant, probably because the New Taipei City is large and the city's general market dynamic does not well correlate with the NTPU-D's condition.

#### *6.3.2. Alternative standard errors*

The shared frailty does not make a notable difference to the results. The contrast between Columns (6) and (7) of [Table 4](#page-9-1) shows. If one then prefers not having the shared frailty, testing alternative standard errors is helpful. The incorporation of time-varying covariates imposes a data structure with repeated observations for subjects and the observations

<span id="page-8-0"></span>**Fig. 3.** Distribution function of time to development

**Panel A: Probability distribution function of Log (Time to development)**

**Panel B:Probability distribution function of time to development**

This figure shows the probability distribution function of time to development and the best fitted lognormal, exponential, and Weibull distributions for it. The actual distribution of time to development is labeled as Kernel. Time to development is the period of waiting between the land acquisition and development. Parameters of distributions are the estimations that best fit the actual data.

<span id="page-9-0"></span>Correlation matrix

This table reports the Pearson correlation matrix of 515 observations from 2000 to 2011. Variance inflation factor (VIF) values, 1/(1 R )*<sup>i</sup>* <sup>2</sup> , are calculated based on the R-square of the OLS which regresses each independent variable *i* on all other covariates. \*\*\*, \*\*, and \* stand for significance at the 1%, 5% and 10% levels, respectively.

|                                                                                                                                  | LN (PC)                                                                                                                      | LN (DC)                                                                                                           | SUB                                                                                                        | LN (DM)                                                                                          | LN (COMN)                                                                       | LN (COMS)                                                          | LN (AP)                                                       | LN(UP)                                         | LN(SIZE)                              | LN (DTMC)             | OS           |
|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------|---------------------------------------|-----------------------|--------------|
| LN (PC)<br>LN (DC)<br>SUB<br>LN (DM)<br>LN (COMN)<br>LN (COMS)<br>LN (AP)<br>LN(UP)<br>LN(SIZE)<br>LN (DTMC)<br>OS<br>VIF values | 1.00<br>0.875⁎⁎⁎<br>0.180⁎⁎⁎<br>0.045<br>-0.317⁎⁎<br>-0.408⁎⁎⁎<br>0.366⁎⁎⁎<br>0.342⁎⁎⁎<br>0.333⁎⁎⁎<br>0.065<br>0.027<br>2.29 | 1.00<br>0.041<br>-0.182⁎⁎⁎<br>-0.437⁎⁎⁎<br>-0.526⁎⁎⁎<br>0.082*<br>0.114⁎⁎⁎<br>0.059<br>0.083*<br>-0.094⁎⁎<br>1.89 | 1.00<br>0.122⁎⁎⁎<br>0.181⁎⁎⁎<br>0.211⁎⁎⁎<br>0.152⁎⁎⁎<br>0.229⁎⁎⁎<br>0.125⁎⁎⁎<br>-0.083*<br>0.094⁎⁎<br>1.38 | 1.00<br>0.101⁎⁎<br>0.316⁎⁎⁎<br>0.442⁎⁎⁎<br>0.124⁎⁎⁎<br>0.450⁎⁎⁎<br>-0.531⁎⁎⁎<br>0.315⁎⁎⁎<br>1.63 | 1.00<br>0.839⁎⁎⁎<br>0.036<br>0.051<br>0.099⁎⁎<br>-0.131⁎⁎⁎<br>-0.120⁎⁎⁎<br>3.13 | 1.00<br>0.051<br>-0.126⁎⁎⁎<br>0.057<br>-0.222⁎⁎⁎<br>-0.013<br>3.07 | 1.00<br>0.329⁎⁎⁎<br>0.993⁎⁎⁎<br>-0.392⁎⁎⁎<br>0.210⁎⁎⁎<br>1.71 | 1.00<br>0.263⁎⁎⁎<br>-0.011<br>0.382⁎⁎⁎<br>1.63 | 1.00<br>-0.416⁎⁎⁎<br>0.183⁎⁎⁎<br>1.91 | 1.00<br>0.064<br>1.40 | 1.00<br>1.21 |

#### <span id="page-9-1"></span>**Table 4**

#### Determinants of development inclination

This table shows the results of the lognormal accelerated failure model of 515 observations from 2000 to 2011. The dependent variable is the time to development, which is the time of waiting since the land acquisition. Time ratio is reported, and standard errors are in parenthesis; \*\*\*, \*\*, and \* stand for significance at the 1%, 5%, and 10% levels, respectively.

|                      | (1)        | (2)        | (3)        | (4)        | (5)        | (6)        | (7)        |
|----------------------|------------|------------|------------|------------|------------|------------|------------|
| Developer            |            |            |            |            |            |            |            |
| LN (PC)              |            | 1.01401    | 1.01913    | 1.03165    | 1.03956    | 1.04868*   | 1.04868*   |
|                      |            | (0.02483)  | (0.02729)  | (0.02899)  | (0.03206)  | (0.03010)  | (0.03010)  |
| LN (DC)              |            |            |            | 0.95706⁎⁎  | 0.95437⁎⁎  | 0.94279⁎⁎⁎ | 0.94278⁎⁎⁎ |
|                      |            |            |            | (0.02107)  | (0.02178)  | (0.02122)  | (0.02122)  |
| SUB                  |            |            |            |            |            | 0.70435⁎⁎⁎ | 0.70440⁎⁎⁎ |
| (1=Yes; 0=No)        |            |            |            |            |            | (0.09011)  | (0.09012)  |
| Market condition     |            |            |            |            |            |            |            |
| LN (DM)              | 0.86130⁎⁎⁎ | 0.86259⁎⁎⁎ | 0.85123⁎⁎⁎ | 0.86021⁎⁎⁎ | 0.85059⁎⁎⁎ | 0.86965⁎⁎⁎ | 0.86965⁎⁎⁎ |
|                      | (0.02425)  | (0.02420)  | (0.02425)  | (0.02654)  | (0.02601)  | (0.02642)  | (0.02642)  |
| LN (COMS)            | 0.73755⁎⁎⁎ | 0.74958⁎⁎⁎ | 0.81432⁎⁎  | 0.72713⁎⁎⁎ | 0.78570⁎⁎  | 0.74231⁎⁎⁎ | 0.74231⁎⁎⁎ |
|                      | (0.62363)  | (0.066639) | (0.08144)  | (0.07081)  | (0.08608)  | (0.07158)  | (0.07159)  |
| Land characteristics |            |            |            |            |            |            |            |
| LN (AP)              | 0.98916    | 0.97648    | 0.97599    | 0.97812    | 0.97669    | 1.00371    | 1.00370    |
|                      | (0.05210)  | (0.05597)  | (0.05333)  | (0.06017)  | (0.05738)  | (0.06166)  | (0.06166)  |
| LN (DTMC)            | 0.95180    | 0.95224    | 0.95418    | 0.95418    | 0.96075    | 0.95407    | 0.95407    |
|                      | (0.05489)  | (0.05500)  | (0.05390)  | (0.05875)  | (0.05805)  | (0.05780)  | (0.05781)  |
| OS                   | 1.11094    | 1.12793    | 1.17027    | 1.11128    | 1.16623    | 1.12085    | 1.12086    |
| (1=Yes; 0=No)        | (0.13108)  | (0.13628)  | (0.13629)  | (0.14608)  | (0.14870)  | (0.14639)  | (0.14639)  |
| Constant             | 650.79⁎⁎⁎  | 524.78⁎⁎⁎  | 209.21⁎⁎⁎  | 865.58⁎⁎⁎  | 358.00⁎⁎⁎  | 423.87⁎⁎⁎  | 423.91⁎⁎⁎  |
|                      | (967.10)   | (802.43)   | (319.27)   | (1445.74)  | (607.96)   | (704.77)   | (704.87)   |
| Shared Frailty       | No         | No         | Yes        | No         | Yes        | No         | Yes        |
| No. of subjects      | 79         | 79         | 79         | 79         | 79         | 79         | 79         |
| No. of obs.          | 515        | 515        | 515        | 515        | 515        | 515        | 515        |
| Log likelihood       | -49.250⁎⁎⁎ | -49.089⁎⁎⁎ | -48.136⁎⁎⁎ | -46.571⁎⁎⁎ | -45.367⁎⁎⁎ | -42.621⁎⁎⁎ | -42.621⁎⁎⁎ |

within each subject are not at all independent.

The findings of the baseline remain robust. The next three columns of [Table 5](#page-10-0) indicate. Columns (3) and (4) apply the robust and bootstrapped standard errors, respectively[.16](#page-9-2) The bootstrapping includes 500 iterations. Results are the same except the significance level of *SUB* reduces to 5%. Since the bootstrapped standard errors and shared frailty are compatible, despite a curse of dimensionality in the computation, we also produce Column (5) that includes both elements. The significance of paid-in capital falls marginally below 10%, but the rest are the same. The estimates are insensitive to unobserved heterogeneity and the data structure.

# *6.3.3. Ordinary least squares*

One might worry that the data structure of repeated observations could give higher weights to the parcels with a longer time to development [\(Cunnungham, 2006](#page-15-16); [Bulan et al., 2009;](#page-14-4) [Groves, 2009](#page-15-17); [Wang et al., 2016\)](#page-15-19). To evaluate, we perform two OLS models, which have a close relationship with the logarithmic AFT. The model of Column (6) is as follows:

$$\ln(T\_{\overline{\mathbb{V}}}) = \beta\_0 + \beta\_1 PC\_{\overline{\mathbb{V}}} + \beta\_2 DC\_{\overline{\mathbb{V}}} + \beta\_3 SUB\_{\overline{\mathbb{V}}} + \beta\_4 DM\_l + \beta\_5 COMS\_l + \beta\_6 AP\_l$$

$$+ \beta\_7 DTMC\_l + \beta\_8 OS\_l + \varepsilon\_{\overline{\mathbb{V}}},\tag{2}$$

It treats *DC* and *COMS* as time-invariant covariates (based on the values at the acquisition date) and has 79 observations. The model of Column (7) recognizes these two variables' time-varying nature (i.e., *DC* and *COMS* can vary quarter by quarter) and has 515 time-varying observations. In both cases, *PC* and *SUB* show significant effects and their signs are consistent with the AFT estimates. In the setting without (with) repeated observations, developers with 1% increase in paid-in

<span id="page-9-2"></span><sup>16</sup> We do not attempt the clustered standard errors, which can bias downward in this case because the number of groups is small ([Donald and Lang, 2007;](#page-15-43) [Cameron et al., 2008](#page-14-10)).

<span id="page-10-0"></span>Robustness tests

This table presents the results of various robustness tests. The dependent variable is the time to development, which is the time of waiting since the land acquisition. COMN is the number of other undeveloped projects located in NTPU-D during the quarter. HPV is the variance of the housing price index of the New Taipei City carried out through a GARCH (1, 1) model. Time ratio is reported, and standard errors are in parentheses; \*\*\*, \*\* and \* stand for significance at the 1%, 5% and 10% levels, respectively.

|                      | COMN as<br>measure of<br>competition | Include House<br>price volatility | Heteroskedasticity-robust<br>standard errors | Bootstrapped<br>standard errors (500<br>times) | Bootstrapped<br>standard errors (500<br>times) | OLS model (79<br>observations) | OLS model (515<br>observations) |
|----------------------|--------------------------------------|-----------------------------------|----------------------------------------------|------------------------------------------------|------------------------------------------------|--------------------------------|---------------------------------|
|                      | (1)                                  | (2)                               | (3)                                          | (4)                                            | (5)                                            | (6)                            | (7)                             |
| Developer            |                                      |                                   |                                              |                                                |                                                |                                |                                 |
| LN (PC)              | 1.056⁎⁎                              | 1.050*                            | 1.049*                                       | 1.049*                                         | 1.049                                          | 0.126*                         | 0.040⁎⁎⁎                        |
|                      | (0.026)                              | (0.030)                           | (0.029)                                      | (0.030)                                        | (0.031)                                        | (0.074)                        | (0.013)                         |
| LN (DC)              | 0.943⁎⁎⁎                             | 0.943⁎⁎⁎                          | 0.943⁎⁎⁎                                     | 0.943⁎⁎⁎                                       | 0.943⁎⁎⁎                                       | -0.071                         | -0.010                          |
|                      | (0.019)                              | (0.021)                           | (0.020)                                      | (0.021)                                        | (0.021)                                        | (0.091)                        | (0.012)                         |
| SUB (1=Yes; 0=No)    | 0.799*                               | 0.707⁎⁎⁎                          | 0.704⁎⁎                                      | 0.704⁎⁎                                        | 0.704⁎⁎                                        | -0.270*                        | -0.438⁎⁎⁎                       |
|                      | (0.095)                              | (0.091)                           | (0.108)                                      | (0.117)                                        | (0.113)                                        | (0.136)                        | (0.053)                         |
| Market condition     |                                      |                                   |                                              |                                                |                                                |                                |                                 |
| LN (DM)              | 0.862⁎⁎⁎                             | 0.870⁎⁎⁎                          | 0.870⁎⁎⁎                                     | 0.870⁎⁎⁎                                       | 0.870⁎⁎⁎                                       | -0.263⁎⁎⁎                      | -0.126⁎⁎⁎                       |
|                      | (0.023)                              | (0.027)                           | (0.021)                                      | (0.022)                                        | (0.024)                                        | (0.049)                        | (0.009)                         |
| LN (HPV)             |                                      | 1.153                             |                                              |                                                |                                                |                                |                                 |
|                      |                                      | (0.335)                           |                                              |                                                |                                                |                                |                                 |
| LN (COMN)            | 0.635⁎⁎⁎                             |                                   |                                              |                                                |                                                |                                |                                 |
|                      | (0.059)                              |                                   |                                              |                                                |                                                |                                |                                 |
| LN (COMS)            |                                      | 0.734⁎⁎⁎                          | 0.742⁎⁎⁎                                     | 0.742⁎⁎⁎                                       | 0.742⁎⁎⁎                                       | 0.320*                         | -0.165⁎⁎⁎                       |
|                      |                                      | (0.073)                           | (0.073)                                      | (0.084)                                        | (0.079)                                        | (0.168)                        | (0.022)                         |
| Land characteristics |                                      |                                   |                                              |                                                |                                                |                                |                                 |
| LN (AP)              | 0.991                                | 0.999                             | 1.004                                        | 1.004                                          | 1.004                                          | -0.026                         | -0.057⁎⁎                        |
|                      | (0.054)                              | (0.062)                           | (0.067)                                      | (0.070)                                        | (0.076)                                        | (0.074)                        | (0.029)                         |
| LN (DTMC)            | 0.968                                | 0.958                             | 0.954                                        | 0.954                                          | 0.954                                          | -0.066                         | -0.112⁎⁎⁎                       |
|                      | (0.051)                              | (0.058)                           | (0.032)                                      | (0.049)                                        | (0.055)                                        | (0.077)                        | (0.029)                         |
| OS (1=Yes; 0=No)     | 1.125                                | 1.115                             | 1.121                                        | 1.121                                          | 1.121                                          | 0.310⁎⁎                        | 0.265⁎⁎⁎                        |
|                      | (0.129)                              | (0.146)                           | (0.135)                                      | (0.136)                                        | (0.144)                                        | (0.149)                        | (0.057)                         |
| Constant             | 58.185⁎⁎⁎                            | 358.009⁎⁎⁎                        | 423.872⁎⁎⁎                                   | 423.873⁎⁎⁎                                     | 423.872⁎⁎⁎                                     | 3.391                          | 10.100⁎⁎⁎                       |
|                      | (65.767)                             | (606.945)                         | (710.852)                                    | (763.625)                                      | (790.337)                                      | (2.410)                        | (0.662)                         |
| Shared Frailty       | Yes                                  | Yes                               | No                                           | No                                             | Yes                                            | No                             | No                              |
| No. of subjects      | 79                                   | 79                                | 79                                           | 79                                             | 79                                             | 79                             | 79                              |
| No. of observations  | 515                                  | 515                               | 515                                          | 515                                            | 515                                            | 79                             | 515                             |
| Log likelihood       | -38.905⁎⁎⁎                           | -42.502⁎⁎⁎                        | -42.621⁎⁎⁎                                   | -42.621⁎⁎⁎                                     | -42.621⁎⁎⁎                                     | Adj. R2<br>: 0.416             | Adj. R2<br>: 0.567              |

capital tend to extend the wait by 0.13% (0.04%), but those involving in subsidiarization are likely to shorten the time by 23.7% (35.5%). The coefficient estimates for the OLS models can be compared with the time ratios (i.e., the expenentiated coefficient *e β* ) for the AFT models. Compared with the AFT estimates, *PC* reveals larger effects on the time to development in the OLS model. The estimates of *DC* have the consistent sign but are insignificant. The effects of land characteristics are stronger and more significant. These results from OLS are for references only since AFT is preferred for survival analysis. The take away is that the basic results are consistent whether or not time-varying covariates are adopted.

#### *6.3.4. Heterogeneous effects*

One might suspect a correlation between developers and lands. Depending on their characteristics, different developers do seem to target different kinds of parcels in usual land auctions. If this stylized correlation applies and both the developer and land features relate to the waiting time, then missing out the land features in the regression can bias the estimates of developer characteristics.

Land quality of NTPU-D is homogeneous, and physical-location variables are observable. Together, they shield the estimation against the above concern. The parcel size is the remaining heterogeneity that they cannot fully address, but the total auction price (unit price × parcel size) can serve as a handle.

For robustness, we control the unit price and parcel size separately. The result is in Column (1) of [Table 6](#page-11-0). The development capacity and subsidiarization remain significantly negative influencing factors of the survival time. The time ratio of paid-in capital is similar to the estimate in Column (7) of [Table 4,](#page-9-1) although it marginally exceeds the 10% level of significance. The time ratio of the unit price is insignificant but large. For the parcel size, the ratio is insignificant and close to one.

In [Table 6,](#page-11-0) we make a further inquiry about whether the relationships between the wait to build and the developer characteristics may depend on the land size. To proceed, we divide the parcels into three groups. The indicator variable *SMALL* is equal to one if the parcel falls below the 33rd percentile of the size distribution, and *LARGE* is one if the land is above the 66th percentile. The regressions of Columns (2), (3), and (4) add the size interaction terms for paid-in capital, development capacity, and subsidiarization, respectively. The relationship of the last developer characteristic with the waiting time appears to be most heterogeneous with respect to the land size.

Column (5) includes all the interaction terms in the regression. The findings discussed thus far are robust for medium sizes of land. Notably, the time ratio of the paid-in capital is now significant at 5%. A 1% more paid-in capital is associated with a significant 0.07% longer wait. A 1% additional development capacity is with a significant 0.08% shorter wait. Developers who practice risk shifting through subsidiarization roughly would significantly shorten the wait by 50%.

<span id="page-11-0"></span>Heterogeneous effects

This table shows the results of the lognormal accelerated failure model of 515 observations from 2000 to 2011. The dependent variable is the wait to build, which is the time of waiting since the land acquisition. Note that SIZE stands for the actual size of the parcel, while SMALL and LARGE are dummy variables. The variable SMALL(LARGE) is equal to one when the land situates in the bottom (top) tercile according to the distribution of SIZE, and zero otherwise. UP is the price per unit of the square meters of the land auctioned. All regression models control for developer's shared frailty. The time ratio is reported, and standard errors are in parenthesis. The asterisks \*\*\*, \*\*, and \* stand for 1%, 5%, and 10% significant levels, respectively.

|                                  | (1)        | (2)        | (3)        | (4)        | (5)        |
|----------------------------------|------------|------------|------------|------------|------------|
| Developer                        |            |            |            |            |            |
| LN (PC) × SMALL                  |            | 0.988      |            |            | 0.922⁎⁎    |
|                                  |            | (0.010)    |            |            | (0.031)    |
| LN (PC) × LARGE                  |            | 1.010      |            |            | 0.989      |
|                                  |            | (0.010)    |            |            | (0.035)    |
| LN (DC) × SMALL                  |            |            | 0.986      |            | 1.067      |
|                                  |            |            | (0.016)    |            | (0.050)    |
| LN (DC) × LARGE                  |            |            | 1.013      |            | 1.024      |
|                                  |            |            | (0.014)    |            | (0.046)    |
| SUB × SMALL                      |            |            |            | 1.486⁎⁎    | 2.574⁎⁎⁎   |
|                                  |            |            |            | (0.291)    | (0.709)    |
| SUB × LARGE                      |            |            |            | 0.897      | 1.111      |
|                                  |            |            |            | (0.176)    | (0.336)    |
| LN (PC)                          | 1.040      | 1.045      | 1.043      | 1.033      | 1.069⁎⁎    |
|                                  | (0.031)    | (0.033)    | (0.032)    | (0.030)    | (0.036)    |
| LN (DC)                          | 0.948⁎⁎    | 0.953*     | 0.952*     | 0.948⁎⁎    | 0.922⁎⁎    |
|                                  | (0.022)    | (0.026)    | (0.026)    | (0.021)    | (0.030)    |
| SUB (1=Yes; 0=No)                | 0.702⁎⁎⁎   | 0.745*     | 0.748*     | 0.630⁎⁎⁎   | 0.494⁎⁎⁎   |
|                                  | (0.089)    | (0.117)    | (0.114)    | (0.096)    | (0.102)    |
| LN (SIZE)                        | 0.981      | 0.842      | 0.868      | 1.087      | 0.845      |
|                                  | (0.065)    | (0.106)    | (0.099)    | (0.092)    | (0.101)    |
| LN (UP)                          | 1.532      | 1.634      | 1.760      | 1.766      | 1.696      |
|                                  | (0.782)    | (1.108)    | (1.107)    | (0.913)    | (0.837)    |
| Market conditions: Suppressed    |            |            |            |            |            |
| Land characteristics: Suppressed |            |            |            |            |            |
| Shared Frailty                   | Yes        | Yes        | Yes        | Yes        | Yes        |
| No. of subjects                  | 79         | 79         | 79         | 79         | 79         |
| No. of obs.                      | 515        | 515        | 515        | 515        | 515        |
| Log likelihood                   | -42.281⁎⁎⁎ | -41.394⁎⁎⁎ | -41.577⁎⁎⁎ | -39.956⁎⁎⁎ | -34.657⁎⁎⁎ |
|                                  |            |            |            |            |            |

The relationship between the development capacity and the wait has no significant heterogeneity in the parcel size. For paid-in capital, its linkage with the waiting time is about the same among large land plots but is significantly weakened and virtually zero among small parcels. For developers involving in the subsidiarization practice, the tendency to shorten the wait is about the same comparing large and medium-sized lands. Nevertheless, that tendency is greatly weakened among the small pieces. The patterns of the heterogeneous effects exhibit high regularity and are not surprising. Indeed, the total development costs for a smaller plot of land is less.

# *6.3.5. A comparison with pseudo samples having the censoring and truncation*

The data free of censoring and truncation indeed facilitate better estimates and address those issues concerned in the literature. To confirm this point, we create three pseudo samples and use them to produce estimates for comparison. For each, we slice off an early period so that the remaining data exhibit a degree of left censoring and truncation.

In [Table 7,](#page-12-0) Panel A indicates the severity of the problem. For example, the most severe case is the sample omitting the observations between 2003 and 2005. It leads to 40 truncated parcels. While 39 subjects are still observable, 32 of them are censored. Panel B compares the estimates from the different samples. Column (1) duplicates the baseline estimates in Column (7) of [Table 4](#page-9-1) and bases on the full sample. The results from the three pseudo samples are in Columns (2) through (4) ordered by the severity in censoring and truncation.

All the standard errors monotonically decrease except one, moving from the first to the fourth column. The standard errors commonly drop by 40% to 50% eventually. Furthermore, the time-ratio estimates also change, and some of these changes exhibit notable differences. These remarkably consistent patterns confirm [Cain et al., \(2011\)](#page-14-5) that the leftcensoring and truncation can substantially bias the estimates and severely underestimate the standard errors. Our data with no censoring and truncation produce more reliable estimates.

# *6.3.6. Institution and policy*

The carrying cost is generally low for developers to hold vacant lands in Taiwan. There is no tax and no maximum holding period. Worried with land banking that can undermine the district's development, the city government launched an incentive scheme on August 8, 2003. As summarized in Panel A of [Table 8,](#page-12-1) the developments that took place within two years from the policy announcement received an 80% additional plot ratio. The incentive reduced to 50% in the third year and then to 20% in the fourth and fifth years. After that, no bonus plot ratio was applicable.

In Panel B, we scrutinize whether taking into consideration the policy would affect the main results. The policy variables are *Bonus*

#### <span id="page-12-0"></span>Effects of censoring and truncation

This table shows the effects of censoring and truncation on regression results. Panel A (B) reports the change in observations (regression results) of each pseudo sample. Time ratio is reported, and standard errors are in parenthesis; \*\*\*, \*\*, and \* stand for significance at the 1%, 5%, and 10% levels, respectively.

| Panel A: Change in observations |             |                   |                    |            |                |  |  |
|---------------------------------|-------------|-------------------|--------------------|------------|----------------|--|--|
|                                 | Subjects    | Censored subjects | Truncated subjects |            | Observations   |  |  |
| Full sample                     | 79 (100%)   | 0 (0%)            | 0 (0%)             |            | 515 (100%)     |  |  |
| Drop obs. in 2003               | 77 (97.4%)  | 19 (24.1%)        | 2 (2.5%)           |            | 403 (78.3%)    |  |  |
| Drop obs. in 2003-2004          | 58 (73.4%)  | 18 (22.8%)        | 21 (26.6%)         |            | 324 (62.9%)    |  |  |
| Drop obs. in 2003-2005          | 39 (49.4%)  | 32 (40.5%)        | 40 (50.6%)         |            | 224 (43.5%)    |  |  |
| Panel B: Regression results     |             |                   |                    |            |                |  |  |
|                                 | Full sample | Drop 2003         | Drop 2003-2004     |            | Drop 2003-2005 |  |  |
|                                 | (1)         | (2)               | (3)                |            | (4)            |  |  |
| Developer                       |             |                   |                    |            |                |  |  |
| LN (PC)                         | 1.049*      | 1.043             | 1.029              |            | 1.074⁎⁎⁎       |  |  |
|                                 | (0.030)     | (0.028)           | (0.024)            |            | (0.022)        |  |  |
| LN (DC)                         | 0.943⁎⁎⁎    | 0.950⁎⁎           | 0.974*             |            | 0.980*         |  |  |
|                                 | (0.021)     | (0.020)           | (0.014)            |            | (0.011)        |  |  |
| SUB (1=Yes; 0=No)               | 0.704⁎⁎⁎    | 0.705⁎⁎⁎          | 0.949              |            | 0.963          |  |  |
|                                 | (0.090)     | (0.088)           | (0.108)            |            | (0.100)        |  |  |
| Market condition                |             |                   |                    |            |                |  |  |
| LN (DM)                         | 0.870⁎⁎⁎    | 0.839⁎⁎⁎          | 0.829⁎⁎⁎           | 0.838⁎⁎⁎   |                |  |  |
|                                 | (0.026)     | (0.021)           | (0.015)            | (0.013)    |                |  |  |
| LN (COMS)                       | 0.742⁎⁎⁎    | 0.770⁎⁎           | 0.847⁎⁎            | 0.907      |                |  |  |
|                                 | (0.072)     | (0.078)           | (0.064)            | (0.062)    |                |  |  |
| Land characteristics            |             |                   |                    |            |                |  |  |
| LN (AP)                         | 1.004       | 1.006             | 1.006              | 0.979      |                |  |  |
|                                 | (0.062)     | (0.059)           | (0.043)            | (0.034)    |                |  |  |
| LN (DTMC)                       | 0.954       | 0.944             | 1.012              | 1.081⁎⁎    |                |  |  |
|                                 | (0.058)     | (0.056)           | (0.045)            | (0.040)    |                |  |  |
| OS (1=Yes; 0=No)                | 1.121       | 1.129             | 1.163*             | 1.113      |                |  |  |
|                                 | (0.146)     | (0.143)           | (0.096)            | (0.084)    |                |  |  |
| Constant                        | 423.91⁎⁎⁎   | 383.10⁎⁎⁎         | 82.49⁎⁎⁎           | 21.44⁎⁎⁎   |                |  |  |
|                                 | (704.87)    | (663.38)          | (100.06)           | (24.07)    |                |  |  |
| Shared Frailty                  | Yes         | Yes               | Yes                | Yes        |                |  |  |
| No. of subjects                 | 79          | 77                | 58                 | 39         |                |  |  |
| No. of obs.                     | 515         | 403               | 324                | 224        |                |  |  |
| Log likelihood                  | -42.621⁎⁎⁎  | -45.013⁎⁎⁎        | -23.064⁎⁎⁎         | -13.766⁎⁎⁎ |                |  |  |
|                                 |             |                   |                    |            |                |  |  |

#### <span id="page-12-1"></span>**Table 8**

Effects of incentive scheme on development inclination

This table shows the effects of incentive schemes on development inclination. Panel A presents the detail of the time-dependent incentive scheme. Panel B reports regression results. The dependent variable is the time to build, which is the time of waiting since the land acquisition. Bonus PRUnexpected (Bonus PRExpected) is the time-varying plot ratio bonus received by the developer according to the size and development time of land parcel for land parcels acquired before (after) August 8, 2003. Time ratio is reported, and standard errors are in parenthesis; \*\*\*, \*\*, and \* stand for significance at the 1%, 5%, and 10% levels, respectively.

| Panel A: Time-dependent incentive scheme                                                                                                              |                                            |                                            |                                           | significant change if the bonus is expected.<br>Offering an unexpected additional plot ratio can accelerate land                                                                                                                                                                                                                                                                                                                                            |  |  |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| Development time<br>August 8, 2003- August 7, 2005<br>August 8, 2005- August 7, 2006<br>August 8, 2006- August 7, 2008<br>Panel B: Regression results | 80%<br>50%<br>20%<br>(1)                   | (2)                                        | (3)                                       | development. For visualization, Figure4 plots the predicted survivor<br>function for four cases. The policy incentive is assumed away in one and<br>is held fixed at a constant level in all others. Without that policy, pro<br>jects will launch at 90% of parcels in 3.46 years of time. When the<br>additional plot ratio applies and stays at 80%, every 9 in 10 parcels will<br>start development within just 1.5 years. The expected wait reduces by |  |  |  |  |
| Developer<br>LN (PC)                                                                                                                                  | 1.045                                      | 1.048                                      | 1.043                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |  |
| LN (DC)                                                                                                                                               | (0.029)<br>0.943⁎⁎⁎<br>(0.021)<br>0.713⁎⁎⁎ | (0.030)<br>0.942⁎⁎⁎<br>(0.021)<br>0.708⁎⁎⁎ | (0.029)<br>0.943⁎⁎⁎<br>(0.021)<br>0.723⁎⁎ | 56.6%.<br>The government's incentive scheme played a vital role fostering land<br>development at NTPU-D. Nevertheless, without an incentive, the pre<br>dicted wait to build would be still remarkably short as compared with                                                                                                                                                                                                                               |  |  |  |  |
| SUB<br>(1=Yes; 0=No)                                                                                                                                  | (0.090)                                    | (0.091)                                    | (0.092)                                   | the general situation in Taiwan. This result is not surprising because the                                                                                                                                                                                                                                                                                                                                                                                  |  |  |  |  |
| Bonus PRUnexpected                                                                                                                                    | 0.828⁎⁎<br>(0.079)                         |                                            | 0.838*<br>(0.082)                         | population growth of NTPU-D was over ten times faster than its<br>neighboring districts; the drift αv was remarkably high.17                                                                                                                                                                                                                                                                                                                                |  |  |  |  |
| Bonus PRExpected                                                                                                                                      |                                            | 1.101<br>(0.336)                           | 1.030<br>(0.047)                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |  |
| Control variable                                                                                                                                      | Yes                                        | Yes                                        | Yes                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |  |
| Shared Frailty                                                                                                                                        | Yes                                        | Yes                                        | Yes                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |  |
| No. of subjects                                                                                                                                       | 79                                         | 79                                         | 79                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |  |
| No. of obs.                                                                                                                                           | 515                                        | 515                                        | 515                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |  |
| Log likelihood                                                                                                                                        | -40.638⁎⁎⁎                                 | -42.572⁎⁎⁎                                 | -40.431⁎⁎⁎                                | 17 The population of NTPU-D had increased 340% between 2000 and 2011,                                                                                                                                                                                                                                                                                                                                                                                       |  |  |  |  |

*PRUnexpected* and *Bonus PRExpected,* which are the time-varying plot-ratio incentives applicable at the project launch. The former (latter) is nonzero only if the land acquisition was before (after) the policy announcement so that the bonus was unexpected (expected). Columns (1) and (2) include only one of the variables, but Column (3) includes both.

The estimates of developer characteristics affirm the previous results. On the incentive, a 1% increase in the permissible plot ratio can significantly reduce the expected wait by 0.16%if this bonus is unexpected, according to Column (3). The impact agrees with the theoretical prediction of [Williams \(1991\).](#page-15-6) Nevertheless, there may be no significant change if the bonus is expected.

<span id="page-12-2"></span>meanwhile those of its two neighboring districts had increased on average 22%.

<span id="page-13-1"></span>**Fig. 4.** Survivor functions of time to development. This figure shows the survivor function of time to development measured in years. Time to development is the time of waiting since the land acquisition. The plot-ratio bonus is assigned based on the incentive scheme launched on August 8, 2003.

#### <span id="page-13-0"></span>**7. Conclusion**

The holding of vacant land has an option value. Existing theory reckons a linkage between the expected wait and the stochastic nature of development costs, but few empirical studies can address that due to data availability. This paper empirically investigates whether the timing to build depends on the characteristics of the developer owning the land, but it also sets out a conceptual framework of a spatial realoption theory that can rationalize our primary and secondary findings.

The main results are threefold. The expected wait is longer for developers with more paid-in capital, which might imply a financing advantage translating to a lower drift in costs. This first finding should be read with caution because of its marginal significance level. Second, developers who currently have less development capacity tend to significantly extend the wait, probably because a construction tie-up at present implies much uncertainty in the additional project's development costs. Third, developers who involve in subsidiarization practices tend to shorten the wait significantly and substantially, because this risk-shifting strategy shields the firms from large losses and reduces the variance of costs.

With complete land auction and development records, our data of the National Taipei University District (NTPU-D) have no censoring and truncation issues. This nice feature advantages the research, compared with the vast majority of survival-analysis studies. To offer external validity, we construct pseudo samples with different levels of severity of the censoring and truncation. The tests on these samples affirm what the literature cautions, the severe underestimation of the standard errors in particular. Our complete data, which are further shielded with homogeneous land quality, facilitate more reliable estimates and significance of the developer characteristics.

The NTPU-D was a successful case in urban planning. The land development process involved private developers' participation but did not encounter a displeasing supply lag. This paper also finds that the time-varying bonus plot-ratio was an effective policy incentive to accelerate the process. The positive market conditions also played a significant role.

The empirical findings of the developers' perspectives on timing-tobuild add useful insights on the cost aspects of the real option literature. We could only find companies' information from public sources. Future research with more detailed data on private developers can study how corporate characteristics influence the behavior in land banking vs. development further. The created knowledge may benefit policy innovation that promotes efficient land development.

#### **CRediT authorship contribution statement**

**Chien-Lin Lu:** Visualization, Writing - review & editing, Writing original draft, Data curation, Investigation, Formal analysis, Validation, Software. **Wen-Chi Liao:** Funding acquisition, Project administration, Supervision, Writing - review & editing, Writing - original draft, Formal analysis, Methodology. **Chien-Wen Peng:** Conceptualization, Resources, Writing - review & editing.

#### **Acknowledgement**

We thank Chin-Oh Chang, Hsiao-Roung Teng, I-Chun Tsai, and seminar participants at the Global Chinese Real Estate Congress 2016 Annual Conference and the 24th Conference of the Chinese Society of Housing Studies. We are grateful to Paul Carrillo and anonymous reviewers' insightful comments and feedback, which allow us to significantly improve the paper. All errors are ours. We sincerely thank the funding support from the Chiang Ching-kuo Foundation for International Scholarly Exchange [Asia-Pacific Region Research Grant RG035-P-12].

#### <span id="page-14-8"></span>**Appendix A: Number of land parcels held by developer**

This figure shows the distribution of the number of parcels held by developers. For example, 20 developers hold only one parcel in the NTPU-D.

### <span id="page-14-9"></span>**Appendix B: Determinants of development inclination using inverse Gaussian distribution of frailty model**

This table shows the results of the lognormal accelerated failure model of 515 observations from 2000 to 2011.The dependent variable is the time to development, which is the period of waiting between the land acquisition and development. Columns (3), (5), and (7) include inverse Gaussian distribution of shared frailty factors. Time ratio is reported, and standard errors are in parenthesis; \*\*\*, \*\*, and \* stand for significance at the 1%, 5%, and 10% levels, respectively.

|                                 | (1)                | (2)                  | (3)                            | (4)                                      | (5)                                      | (6)                                  | (7)                                  |
|---------------------------------|--------------------|----------------------|--------------------------------|------------------------------------------|------------------------------------------|--------------------------------------|--------------------------------------|
| Developer<br>LN (PC)<br>LN (DC) |                    | 1.01401 (0.02483)    | 1.01826 (0.02720)              | 1.03165 (0.02899)<br>0.95706⁎⁎ (0.02107) | 1.03958 (0.03261)<br>0.95287⁎⁎ (0.02213) | 1.04868* (0.03010)<br>0.94279⁎⁎⁎     | 1.04868* (0.03010)<br>0.94278⁎⁎⁎     |
| SUB (1=Yes;<br>0=No)            |                    |                      |                                |                                          |                                          | (0.02122)<br>0.70435⁎⁎⁎<br>(0.09011) | (0.02122)<br>0.70436⁎⁎⁎<br>(0.09011) |
| Market condition                |                    |                      |                                |                                          |                                          |                                      |                                      |
| LN (DM)                         | 0.86130⁎⁎⁎         | 0.86259⁎⁎⁎ (0.02420) | 0.85422⁎⁎⁎                     | 0.86021⁎⁎⁎                               | 0.85215⁎⁎⁎                               | 0.86965⁎⁎⁎                           | 0.86964⁎⁎⁎                           |
|                                 | (0.02425)          |                      | (0.02463)                      | (0.02654)                                | (0.02632)                                | (0.02642)                            | (0.02642)                            |
| LN (COMS)                       | 0.73755⁎⁎⁎         | 0.74958⁎⁎⁎           | 0.79895⁎⁎ (0.07992) 0.72713⁎⁎⁎ |                                          | 0.77796⁎⁎ (0.08399)                      | 0.74231⁎⁎⁎                           | 0.74233⁎⁎⁎                           |
|                                 | (0.62363)          | (0.066639)           |                                | (0.07081)                                |                                          | (0.07158)                            | (0.07158)                            |
| Land characteristics            |                    |                      |                                |                                          |                                          |                                      |                                      |
| LN (AP)                         | 0.98916 (0.05210)  | 0.97648 (0.05597)    | 0.97615 (0.05394)              | 0.97812 (0.06017)                        | 0.97664 (0.05781)                        | 1.00371 (0.06166)                    | 1.00372 (0.06160)                    |
| LN (DTMC)                       | 0.95180 (0.05489)  | 0.95224 (0.05500)    | 0.95522 (0.05446)              | 0.95418 (0.05875)                        | 0.96205 (0.05877)                        | 0.95407 (0.05780)                    | 0.95407 (0.05780)                    |
| OS (1=Yes; 0=No)                | 1.11094 (0.13108)  | 1.12793 (0.13628)    | 1.16302 (0.13777)              | 1.11128 (0.14608)                        | 1.16235 (0.14999)                        | 1.12085 (0.14639)                    | 1.12088 (0.14639)                    |
| Constant                        | 650.79⁎⁎⁎ (967.10) | 524.78⁎⁎⁎ (802.43)   | 254.34⁎⁎⁎ (396.73)             | 865.58⁎⁎⁎ (1445.74)                      | 399.61⁎⁎⁎ (680.62)                       | 423.87⁎⁎⁎ (704.77)                   | 423.72⁎⁎⁎ (704.51)                   |
| Shared Frailty                  | No                 | No                   | Yes                            | No                                       | Yes                                      | No                                   | Yes                                  |
| No. of subjects                 | 79                 | 79                   | 79                             | 79                                       | 79                                       | 79                                   | 79                                   |
| No. of obs.                     | 515                | 515                  | 515                            | 515                                      | 515                                      | 515                                  | 515                                  |
| Log likelihood                  | -49.250⁎⁎⁎         | -49.089⁎⁎⁎           | -48.403⁎⁎⁎                     | -46.571⁎⁎⁎                               | -45.517⁎⁎⁎                               | -42.621⁎⁎⁎                           | -42.621⁎⁎⁎                           |

#### **Reference**

- <span id="page-14-0"></span>Alig, R., Kline, J.D., Lichtenstein, M., 2004. Urbanization on the US landscape: looking ahead in the 21st century. Landscape and Urban Planning 69, 219–234. [https://doi.](https://doi.org/10.1016/j.landurbplan.2003.07.004) [org/10.1016/j.landurbplan.2003.07.004](https://doi.org/10.1016/j.landurbplan.2003.07.004).
- <span id="page-14-1"></span>Asfour, O.S., 2012. Towards an effective strategy to cope with housing land scarcity in the Gaza Strip as a sustainable development priority. Habitat International 36, 295–303. <https://doi.org/10.1016/j.habitatint.2011.10.005>.
- <span id="page-14-4"></span>Bulan, L., Mayer, C., Somerville, C.T., 2009. Irreversible investment, real options, and competition: evidence from real estate development. Journal of Urban Economics 65, 237–251. [https://doi.org/10.1016/j.jue.2008.03.003.](https://doi.org/10.1016/j.jue.2008.03.003)
- <span id="page-14-5"></span>Cain, K.C., Harlow, S.D., Little, R.J., Nan, B., Yosef, M., Taffe, J.R., Elliott, M.R., 2011. Bias due to left truncation and left censoring in longitudinal studies of developmental

and disease processes. American Journal of Epidemiology 173, 1078–1084. [https://](https://doi.org/10.1093/aje/kwq481) [doi.org/10.1093/aje/kwq481](https://doi.org/10.1093/aje/kwq481).

- <span id="page-14-10"></span>Cameron, A.C., Gelbach, J.B., Miller, D.L., 2008. Bootstrap-based improvements for inference with clustered errors. Review of Economics and Statistics 90, 414–427. [https://doi.org/10.1162/rest.90.3.414.](https://doi.org/10.1162/rest.90.3.414)
- <span id="page-14-2"></span>Capozza, D.R., Helsley, R.W., 1990. The stochastic city. Journal of Urban Economics 28, 187–203. [https://doi.org/10.1016/0094-1190\(90\)90050-W.](https://doi.org/10.1016/0094-1190(90)90050-W)
- <span id="page-14-3"></span>Capozza, D.R., Li, Y., 1994. The intensity and timing of investment: the case of land. American Economic Review 84 (4), 889–904. [https://www.jstor.org/stable/](https://www.jstor.org/stable/2118036) [2118036.](https://www.jstor.org/stable/2118036)

<span id="page-14-6"></span>[Chan, S.H., Fang, F., Yang, J., 2008. Presales, financing constraints, and developers'](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0008) [production decisions. Journal of Real Estate Research 30, 345–375](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0008).

<span id="page-14-7"></span>[Chan, S.H., Fang, F., Yang, J., 2014. Presales, leverage decisions, and risk shifting.](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0009) [Journal of Real Estate Research 36, 475–509.](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0009)

- <span id="page-15-22"></span>Chau, K.W., Wong, S.K., Yiu, C.Y., 2007. Housing quality in the forward contracts market. Journal of Real Estate Finance and Economics 34, 313–325. [https://doi.org/10.](https://doi.org/10.1007/s11146-007-9018-x) [1007/s11146-007-9018-x](https://doi.org/10.1007/s11146-007-9018-x).
- <span id="page-15-24"></span>[Chiang, Y., Huang, C., Sa-Aadu, J., 2004. The pricing of purchase discount options in](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0011) [Taiwanese pre-sale housing market. Working paper.](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0011)
- <span id="page-15-37"></span>[Cox, D.R., Oakes, D., 1984. Analysis of Survival Data. Chapman and Hall, London](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0012).
- <span id="page-15-16"></span>Cunningham, C., 2006. House price uncertainty, timing of development, and vacant land prices: evidence for real options in Seattle. Journal of Urban Economics 59, 1–31. <https://doi.org/10.1016/j.jue.2005.08.003>.
- <span id="page-15-30"></span>Dell'Ariccia, G., Marquez, R., 2010. Risk and the corporate structure of banks. Journal of Finance 65, 1075–1096. [https://www.jstor.org/stable/25656321.](https://www.jstor.org/stable/25656321)
- <span id="page-15-43"></span>Donald, S.G., Lang, K., 2007. Inference with difference-in-differences and other panel data. Review of Economics and Statistics 89, 221–233. [https://doi.org/10.1162/rest.](https://doi.org/10.1162/rest.89.2.221) [89.2.221.](https://doi.org/10.1162/rest.89.2.221)
- <span id="page-15-8"></span>Dong, Z., Sing, T.F., 2017. Developers' heterogeneity and real estate development timing options. Journal of Property Investment and Finance 35, 472–488. [https://doi.org/](https://doi.org/10.1108/JPIF-07-2016-0058) [10.1108/JPIF-07-2016-0058](https://doi.org/10.1108/JPIF-07-2016-0058).
- <span id="page-15-38"></span>Efron, B., 1977. The efficiency of Cox's likelihood function for censored data. Journal of the American Statistical Association 72, 557–565. [https://doi.org/10.2307/2286217.](https://doi.org/10.2307/2286217)
- <span id="page-15-34"></span>Grenadier, S.R., 1996. The strategic exercise of options: development cascades and overbuilding in real estate markets. Journal of Finance 51, 1653–1679. [https://doi.](https://doi.org/10.2307/2329533) [org/10.2307/2329533.](https://doi.org/10.2307/2329533)
- <span id="page-15-11"></span>Grovenstein, R.A., Kau, J.B., Munneke, H.J., 2011. Development value: a real options approach using empirical data. Journal of Real Estate Finance and Economics 43, 321–335. <https://doi.org/10.1007/s11146-010-9277-9>.
- <span id="page-15-17"></span>Groves, J.R., 2009. The impact of positive property tax differentials on the timing of development. Regional Science and Urban Economics 39, 739–748. [https://doi.org/](https://doi.org/10.1016/j.regsciurbeco.2009.07.004) [10.1016/j.regsciurbeco.2009.07.004.](https://doi.org/10.1016/j.regsciurbeco.2009.07.004)
- <span id="page-15-10"></span>Guthrie, G., 2010. House prices, development costs, and the value of waiting. Journal of Urban Economics 68, 56–71. [https://doi.org/10.1016/j.jue.2010.02.002.](https://doi.org/10.1016/j.jue.2010.02.002)
- <span id="page-15-41"></span>Gutierrez, R.G., 2002. Parametric frailty and shared frailty survival models. The Stata Journal 2, 22–44. <https://doi.org/10.1177/1536867x0200200102>.
- <span id="page-15-0"></span>Iwata, O., Oguchi, T., 2009. Factors affecting late twentieth century land use patterns in Kamakura City, Japan. Geographical Research 47, 174–191. [https://doi.org/10.](https://doi.org/10.1111/j.1745-5871.2008.00559.x) [1111/j.1745-5871.2008.00559.x](https://doi.org/10.1111/j.1745-5871.2008.00559.x).
- <span id="page-15-29"></span>Kahn, C., Winton, A., 2004. Moral hazard and optimal subsidiary structure for financial institutions. Journal of Finance 59, 2531–2575. [https://www.jstor.org/stable/](https://www.jstor.org/stable/3694781) [3694781.](https://www.jstor.org/stable/3694781)
- <span id="page-15-1"></span>Kong, L., 2012. No place, new places: death and its rituals in urban Asia. Urban Studies 49, 415–433. <https://doi.org/10.1177/0042098011402231>.
- <span id="page-15-15"></span>Kremer, P., Hamstead, Z.A., McPhearson, T., 2013. A social-ecological assessment of vacant lots in New York City. Landscape and Urban Planning 120, 218–233. [https://](https://doi.org/10.1016/j.landurbplan.2013.05.003) [doi.org/10.1016/j.landurbplan.2013.05.003.](https://doi.org/10.1016/j.landurbplan.2013.05.003)
- <span id="page-15-28"></span>Lagakos, S.W., 1979. General right censoring and its impact on the analysis of survival data. Biometrics 35, 13–156. [https://doi.org/10.2307/2529941.](https://doi.org/10.2307/2529941)
- <span id="page-15-23"></span>Lai, R.N., Wang, K., Zhou, Y., 2004. Sale before completion of development: pricing and strategy. Real Estate Economics 32, 329–357. [https://doi.org/10.1111/j.1080-8620.](https://doi.org/10.1111/j.1080-8620.2004.00094.x) [2004.00094.x.](https://doi.org/10.1111/j.1080-8620.2004.00094.x)
- <span id="page-15-40"></span>Lambert, P., Collett, D., Kimber, A., Johnson, R., 2004. Parametric accelerated failure time models with random effects and an application to kidney transplant survival. Statistics in Medicine 23, 3177–3192. <https://doi.org/10.1002/sim.1876>.
- <span id="page-15-26"></span>Lee, M.-L.T., Whitmore, G.A., 2006. Threshold regression for survival analysis: modeling event times by a stochastic process reaching a boundary. Statistical Science 21, 501–513. <https://www.jstor.org/stable/27645791>.
- <span id="page-15-27"></span>Leung, K., Elashoff, R.M., Afifi, A.A., 1997. Censoring issues in survival analysis. Annual Reviews of Public Health 18, 83–104. [https://doi.org/10.1146/annurev.publhealth.](https://doi.org/10.1146/annurev.publhealth.18.1.83) [18.1.83](https://doi.org/10.1146/annurev.publhealth.18.1.83).
- <span id="page-15-25"></span>[Leung, B., Hui, E., Seabrooke, B., 2007. Pricing of presale properties with asymmetric](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0032) [information problems. Journal of Real Estate Portfolio Management 13, 139–152](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0032).
- <span id="page-15-42"></span>Liao, W., Zhao, D., Lim, L.P., Wong, G.K.M., 2015. Foreign liquidity to real estate market: ripple effect and housing price dynamics. Urban Studies 52, 138–158. [https://doi.](https://doi.org/10.1177/0042098014523687) [org/10.1177/0042098014523687.](https://doi.org/10.1177/0042098014523687)
- <span id="page-15-3"></span>[Mayer, C., Somerville, C.T., 2000. Land use regulation and new construction. Regional](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0034) [Science and Urban Economics 30, 639–662.](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0034)
- <span id="page-15-5"></span>McDonald, R., Siegel, D., 1986. The value of waiting to invest. Quarterly Journal of Economics 101, 707–728. [https://www.jstor.org/stable/1884175.](https://www.jstor.org/stable/1884175)
- <span id="page-15-36"></span>Miles, W., 2009. Irreversibility, uncertainty and housing investment. Journal of Real Estate Finance and Economics 38, 173–182. [https://doi.org/10.1007/s11146-007-](https://doi.org/10.1007/s11146-007-9087-x) [9087-x](https://doi.org/10.1007/s11146-007-9087-x).
- <span id="page-15-39"></span>Oakes, D., 1977. The asymptotic information in censored survival data. Biometrica 64, 441–448. <https://doi.org/10.2307/2345319>.
- <span id="page-15-31"></span>Ogu, V.I., Ogbuozobe, J.E., 2001. Housing policy in Nigeria: towards enablement of private housing development. Habitat International 25, 473–492. [https://doi.org/10.](https://doi.org/10.1016/S0197-3975(01)00018-2) [1016/S0197-3975\(01\)00018-2.](https://doi.org/10.1016/S0197-3975(01)00018-2)
- <span id="page-15-4"></span>Quigley, J., Raphael, S., 2005. Regulation and the high costs of housing in California. American Economic Review 95, 323–328. [https://doi.org/10.1257/](https://doi.org/10.1257/000282805774670293) [000282805774670293](https://doi.org/10.1257/000282805774670293).
- <span id="page-15-14"></span>[Pagano, M.A., Bowman, A.O., 2000. Vacant Land in cities: An urban Resource. The](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0040) [Brookings Institution Survey Series, Washington, DC](http://refhub.elsevier.com/S1051-1377(20)30045-0/sbref0040).
- <span id="page-15-9"></span>Quigg, L., 1993. Empirical testing of real option pricing models. Journal of Finance 48 (2), 621–640. <https://doi.org/10.2307/2328915>.
- <span id="page-15-21"></span>Shen, J., Pretorius, F., 2013. Binomial option pricing models for real estate development. Journal of Property Investment and Finance 31, 418–440. [https://doi.org/10.1108/](https://doi.org/10.1108/JPIF-10-2012-0046) [JPIF-10-2012-0046.](https://doi.org/10.1108/JPIF-10-2012-0046)
- <span id="page-15-35"></span>Somerville, C., 2001. Permits, starts and completions: structural relationships versus real options. Real Estate Economics 1, 161–190. [https://doi.org/10.1111/1080-8620.](https://doi.org/10.1111/1080-8620.00006) [00006.](https://doi.org/10.1111/1080-8620.00006)
- <span id="page-15-2"></span>Titman, S., 1985. Urban land prices under uncertainty. American Economic Review 75 (3), 505–514. [http://www.jstor.org/stable/1814815?origin=JSTOR-pdf.](http://www.jstor.org/stable/1814815?origin=JSTOR-pdf)
- <span id="page-15-12"></span>Tsekrekos, A.E., Kanoutos, G., 2013. Real option premia implied from recent transactions in the Greek real estate market. Journal of Real Estate Finance and Economics 47, 152–168. [https://doi.org/10.1007/s11146-011-9350-z.](https://doi.org/10.1007/s11146-011-9350-z)
- <span id="page-15-33"></span>Turok, I., 2016. Housing and the urban premium. Habitat International 54, 234–240. <https://doi.org/10.1016/j.habitatint.2015.11.019>.
- <span id="page-15-20"></span>Wang, K., Zhou, Y., 2000. Overbuilding: a game-theoretic approach. Real Estate Economics 28, 493–522. [https://doi.org/10.1111/1540-6229.00810.](https://doi.org/10.1111/1540-6229.00810)
- <span id="page-15-7"></span>Wang, K., Zhou, Y., 2006. Equilibrium real options exercise strategies with multiple players: the case of real estate markets. Real Estate Economics 34, 1–49. [https://doi.](https://doi.org/10.1111/j.1540-6229.2006.00158.x) [org/10.1111/j.1540-6229.2006.00158.x.](https://doi.org/10.1111/j.1540-6229.2006.00158.x)
- <span id="page-15-19"></span>Wang, Y., Tang, W., Jia, S., 2016. Uncertainty, competition and timing of land development: theory and empirical evidence from Hangzhou, China. Journal of Real Estate Finance and Economics 53, 218–245. <https://doi.org/10.1007/s11146-015-9517-0>.
- <span id="page-15-6"></span>Williams, J.T., 1991. Real estate development as an option. Journal of Real Estate Finance and Economics 4 (2), 191–208. [https://doi.org/10.1007/BF00173124.](https://doi.org/10.1007/BF00173124)
- <span id="page-15-18"></span>Wrenn, D.H., Irwin, E.G., 2015. Time is money: an empirical examination of the effects of regulatory delay on residential subdivision development. Regional Science and Urban Economics 51, 25–36. <https://doi.org/10.1016/j.regsciurbeco.2014.12.004>.
- <span id="page-15-32"></span>Wu, W., Dong, G., Wang, B., 2015. Does planning matter? Effects on land markets. Journal of Real Estate Finance and Economics 50, 242–269. [https://doi.org/10.](https://doi.org/10.1007/s11146-014-9455-2) [1007/s11146-014-9455-2](https://doi.org/10.1007/s11146-014-9455-2).
- <span id="page-15-13"></span>Yang, Z., Wu, S., 2019. Land acquisition outcome, developer risk attitude and land development timing. Journal of Real Estate Finance and Economics 59, 233–271. [https://doi.org/10.1007/s11146-018-9663-2.](https://doi.org/10.1007/s11146-018-9663-2)