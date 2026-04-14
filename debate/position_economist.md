# Academic Integrity and AI Fraud: An Economic Analysis

**Position Paper — Economics of Education Perspective**

*Framing: Gary Becker's human capital theory, Michael Spence's signaling model (1973), George Akerlof's market for lemons (1970), and empirical education economics in the tradition of Hanushek, Hoxby, and Chetty.*

---

## 1. The Economic Diagnosis: A Signal Degradation Crisis

Academic credentials function, in Spence's (1973) original formulation, as costly signals that separate high-productivity from low-productivity workers in labor markets characterized by asymmetric information. A degree signals two things simultaneously: (a) the holder completed a costly investment (four years, tuition, opportunity cost), which low-ability workers would find unprofitable; and (b) the institution certified that the holder met explicit competency standards.

Generative AI has broken the second component of this signal at negligible marginal cost.

Before November 2022, producing a credibly university-quality essay required either genuine competency or expensive contract cheating (Newton 2018 estimated the global contract cheating market at 15.7% of students paying third parties — a non-trivial direct cost that constituted the sorting mechanism). After November 2022, the marginal cost of submitting AI-generated work collapsed to approximately zero. The sorting mechanism that made credential signals informative has been destroyed.

The Springer 2024 study of 1,386 Vietnamese undergraduates — using a list experiment methodology that bypasses self-report bias — found that actual AI cheating prevalence is **approximately 3x the self-reported rate**. Applying this to Vietnam's approximately 2.1 million undergraduates (MOET 2023), we are likely looking at hundreds of thousands of students per year submitting partially or wholly AI-generated work while reporting otherwise. This is not a marginal compliance problem. This is a market failure.

---

## 2. Market Failures in the Current System

### 2.1 Akerlof's Market for Lemons — Applied to Credentials

Akerlof (1970) demonstrated that in markets where sellers know quality and buyers do not, adverse selection drives out high-quality goods. Apply this to the diploma market:

- **Sellers** (graduates) know whether their degree reflects genuine competency or AI-substituted work.
- **Buyers** (employers, graduate admissions, professional licensing bodies) cannot observe this distinction from the credential alone.
- **Result**: Employers rationally discount the signal value of degrees from institutions with known AI fraud problems.

The evidence supports this adverse selection dynamic already playing out. UK employer surveys (post-Sheffield's FOI disclosure showing a 15x increase in AI misconduct cases, from 6 in 2022-23 to 92 in 2023-24) show growing employer skepticism. Springer Nature's 2,923 retractions in 2024 — the highest single-publisher annual retraction count in history — demonstrate that the lemons problem has already entered the credentialing market for research outputs, not just undergraduate degrees.

The long-run equilibrium of unchecked AI fraud is **credential inflation**: every employer must spend more on verification (practical tests, extended probationary periods, professional certifications that supplement degrees) to achieve the same information that degrees previously provided. This is a pure deadweight loss.

### 2.2 Negative Externalities — Who Bears the Cost?

The individual student who submits AI-generated work captures private benefits (a passing grade, progression, a credential) while imposing costs on:

1. **Other students**: Honest students are assessed against a distribution in which AI fraud inflates apparent performance, compressing grade distributions and reducing relative signal quality of authentic work. If grading is curved or ranked, AI fraud is a direct transfer from honest to dishonest students.

2. **Employers**: Bear search costs of screening out credential-holders without genuine competency (back-of-envelope: if 20% of graduates have AI-inflated credentials and average hiring costs in Vietnam are ~2-3 months' salary, the economy-wide screening cost increment is non-trivial at scale).

3. **The scientific knowledge base**: The Hindawi/Wiley mass retraction of 8,000+ papers in 2023-2024, and NeurIPS 2025's 100+ hallucinated citations in 51 accepted papers, demonstrate that AI fraud in research produces contaminated information goods that propagate through citation networks. A retracted neurosurgery paper citing fabricated drug efficacy data is not merely a private loss.

4. **The state**: Vietnam's education strategy QĐ 1705/QĐ-TTg targets Vietnamese universities achieving ASEAN-leading research quality by 2030. If AI fraud is degrading research outputs, the state's investment in research infrastructure (targeting minimum 20% of state budget in education) generates lower social returns than projected.

These externalities are classic justification for public intervention — the private cost-benefit calculation of AI fraud does not account for social costs.

### 2.3 Public Goods and Information Asymmetry in the Detection Market

Detection tools (Turnitin AI Detection, GPTZero) are private goods sold to institutions, creating a market structure problem:

- **Turnitin quasi-monopoly**: Turnitin holds dominant market share in institutional plagiarism and AI detection. Its AI detection module (launched April 2023) claims 98% accuracy but Washington Post independent testing found approximately 50% real-world accuracy. The gap between claimed and actual performance is a classic information asymmetry — institutions are buyers with limited ability to audit the performance claims of the seller.
- **Rent extraction**: Turnitin's institutional subscription model means that universities pay recurring rents for a product whose core function (authentic work verification) is not being delivered at the claimed quality. This is a straightforward case of market failure due to information asymmetry between a sophisticated technology seller and institutional buyers who lack the technical capacity to conduct independent validation.
- **Switching costs**: Universities that have integrated Turnitin into LMS infrastructure, trained faculty, and built policy procedures around it face substantial switching costs. These switching costs allow Turnitin to extract rents above competitive equilibrium pricing, under-invest in accuracy improvements, and resist independent auditing.

The Liang et al. (Stanford HAI, 2023) finding that GPTZero produces a **61.3% false positive rate on TOEFL essays** (i.e., human-written English essays by non-native speakers flagged as AI-generated) is not just an accuracy problem — it is evidence of systematic discriminatory market failure. A detection tool that is substantially less accurate for non-native English writers creates an implicit tax on non-native English-speaking students: they bear disproportionate enforcement risk for behavior they did not commit. In Vietnam's context, where essentially all higher education operates through Vietnamese-language or Vietnamese-accented English writing, this is a catastrophic product defect being sold at premium institutional prices.

---

## 3. The Arms Race Problem: Infinite Escalation, No Durable Equilibrium

The detection-versus-evasion dynamic is a classic arms race game theory problem with no stable equilibrium:

- Detection tools (Turnitin AI, GPTZero) improve → AI humanization tools (Undetectable.ai, QuillBot, HIX.AI) specifically retrain to evade improved detection → detection tools retrain → cycle repeats.

This is an infinite-horizon game in which **neither player can win decisively**. The economic implications are important:

1. **Resource dissipation**: Both detection companies and evasion tool developers are investing real resources in cancelling each other out. This is pure rent-seeking with no social value creation — a welfare loss equivalent to the famous lighthouse problem in public goods theory.

2. **Who funds the arms race?** Universities (institutional subscribers) and students (tuition, which partly funds institutional overhead including Turnitin contracts). The costs of the arms race are borne by the education sector, not by the technology companies whose products created the underlying distortion.

3. **Asymmetric incentives**: Detection companies benefit commercially from the arms race (escalation justifies annual subscription renewals and product upgrades). Evasion tool companies similarly benefit. Universities — the ultimate payers — have no ability to exit the arms race without abandoning enforcement entirely.

The arms race is a coordination failure. No individual institution can unilaterally exit because if they stop detection and competitors do not, their credentials are disproportionately devalued. This is a prisoners' dilemma structure: the dominant strategy for each institution is to invest in detection even though collective investment in detection produces an inefficient equilibrium.

The economically rational response to a prisoners' dilemma is **coordination** — either through regulation (mandatory national standards) or through assessment redesign that eliminates the game board entirely.

---

## 4. Human Capital vs. Signal: What Is Actually Being Destroyed?

Becker's (1964) human capital theory and Spence's (1973) signaling model make different predictions about the social cost of AI fraud, and the distinction matters for policy:

**Becker's view**: Education produces human capital — actual skills, knowledge, and productivity that increase worker output. Under this view, AI fraud destroys human capital formation. A medical student who passes clinical pharmacology exams using ChatGPT (Newton & Xiromeriti 2023 showed ChatGPT passes medical assessments) has not developed clinical reasoning ability. The social cost is a doctor who will make worse patient decisions — a direct productivity loss.

**Spence's view**: Education is primarily a signal — it sorts workers by pre-existing ability. Under this view, AI fraud degrades the signal without necessarily destroying human capital (the high-ability worker who would have learned anyway just used a more efficient tool). The social cost is the loss of sorting efficiency, not the loss of skill development.

**The empirical answer**: Both are occurring simultaneously, but the human capital destruction is the more serious concern for Vietnam's context. Vietnam is not in a mature economy where workers would have acquired skills through on-the-job training regardless of formal education. In a development economics context (Hanushek & Woessmann 2012 demonstrated that cognitive skills, not just credentials, drive long-run economic growth), credential inflation without corresponding human capital development is a growth-retarding force.

The Springer 2024 Vietnamese data (3x concealment rate) combined with QĐ 1705's competency-based education mandate creates a contradiction: the state is explicitly targeting competency development, but the actual education system is producing credential holders who are substituting AI output for genuine competency acquisition. This is a strategic policy failure with measurable long-run GDP implications.

---

## 5. Incentive Misalignment: The Cost-Benefit Calculation of AI Fraud

Students respond to incentives. The decision to commit AI fraud is a rational expected-utility calculation:

**Expected benefit**: Grade improvement × probability of successful evasion × labor market premium of credential upgrade

**Expected cost**: Penalty severity × probability of detection

Current calibration of this calculation strongly favors fraud:

- **Probability of detection**: Low and declining. The arms race dynamics described above mean students who apply basic humanization techniques evade detection with high probability. The 3x concealment rate in the Springer 2024 Vietnamese study implies an extremely high successful-evasion rate.
- **Penalty severity**: Variable and frequently lenient. Vietnam's HCMUFA case (the first publicly reported Vietnamese AI fraud case, 2023) resulted in a 50% score deduction — the softest sanction in the regional Asian peer set (compared to CUHK expulsions and NTU zero marks). Inconsistent penalty schedules further reduce deterrence.
- **Benefit**: In Vietnam's labor market, the credential premium is high relative to income levels. A university degree commands substantially higher wages than the alternative, and grade performance affects graduate school admission, competitive employer selection, and scholarship access. The stakes are high.

This incentive structure will not self-correct. The rational response to an expected value calculation that rewards fraud is not moral exhortation — it is recalibrating the calculation by raising the probability of detection, increasing penalty severity, or reducing the benefit of fraud (which in practice means ensuring that genuine competency is verified in ways AI cannot substitute).

---

## 6. Evaluation of Interventions: Efficiency Analysis

### 6.1 Economically Efficient Interventions

**Assessment redesign (oral defense, process-based assessment)**: This is the highest-efficiency intervention. By making AI substitution structurally impossible rather than detection-dependent, it eliminates the arms race game board. The spot viva model (random 10-20% sampling for oral follow-up examination) is particularly cost-effective: at 15-20 minutes per student, a 10% random sample of a 300-student cohort requires approximately 10 hours of examiner time per assessment cycle. This is a positive-NPV investment: it eliminates the recurring costs of detection tool licensing, false positive adjudication, and disciplinary proceedings, while restoring signal quality. The University of Western Ontario's 600-student oral exam implementation is direct evidence of operational scalability.

The AIAS framework (Perkins, British University Vietnam 2023) — developed specifically in the Vietnamese context — provides a tiered cost-benefit structure for assessment design: Tier 1-2 assessments (AI prohibited) for high-human-capital-development tasks; Tier 4-5 assessments (AI integrated) for AI-collaboration skill development. This is efficient because it targets detection costs only where the human capital stakes are highest, and eliminates enforcement costs entirely in contexts where AI use is legitimate.

**Process-based assessment (staged submissions, revision history)**: Moderate efficiency. Google Workspace revision history is available at zero marginal cost to institutions on Google for Education programs. The incremental cost is faculty time for reviewing process evidence. The efficiency gain is substantial relative to detection tools: no false positive problem, no arms race, direct measurement of genuine learning process.

**LLM watermarking (if mandated by regulation)**: Potentially the highest long-run efficiency solution, but currently a public goods problem. No major LLM provider has deployed production text watermarking (Aaronson disclosed that OpenAI built a functional system but declined deployment, citing competitive disadvantage). The collective action barrier requires regulatory mandate to overcome — EU AI Act Article 50 is moving in this direction. For Vietnam, advocating for watermarking through ASEAN AI governance forums costs little and positions Vietnam to benefit from multilateral solutions.

**Honor code culture investment (McCabe model)**: High long-run efficiency, low short-run measurability. McCabe's 30-year research program across 70,000+ students found that institutions with genuine honor code cultures show 25-30% lower self-reported cheating rates. The ROI on culture investment is real but has long payback periods — unsuitable as a sole response to an acute problem but essential as the durable long-run solution.

### 6.2 Economically Wasteful Interventions

**Exclusive reliance on AI detection tools**: Negative expected value once false positive costs are properly accounted for. The 61.3% false positive rate on TOEFL essays (Liang et al. Stanford 2023) means that for every confirmed AI fraud case caught by detection tools in a Vietnamese English-medium course, 0.6+ innocent students are wrongfully accused. At a conservative estimate of adjudication costs (faculty time, student psychological harm, potential grade appeal proceedings), the total cost of false positives likely exceeds the benefit of true positive detections. This is a standard type I error rate problem in statistical decision theory: when base rates of true positives are moderate and the cost of false positives is high, a classifier with a 60%+ false positive rate should not be used as a primary enforcement mechanism.

Detection tools may have marginal value as a **flag-for-review** trigger (not as a standalone penalty basis), but this use case requires institutional understanding that detection scores are probabilistic inputs to human judgment, not verdicts.

**Blanket AI prohibition policies (CUHK model)**: Economically inefficient for two reasons. First, prohibition without enforcement is meaningless (as the 3x concealment rate demonstrates — students already know they should not cheat and conceal it anyway). A prohibition without structural verification is a policy with zero enforcement teeth. Second, blanket prohibition prevents legitimate human capital gains from AI tool mastery. In a labor market where AI collaboration skills command premium wages, an education system that prevents AI skill development is reducing the economic returns to education for its graduates — a welfare-reducing policy from a human capital perspective.

**Escalating surveillance infrastructure (biometric proctoring, AI behavior monitoring)**: The privacy costs, false positive risks, and adversarial dynamics of surveillance-based assessment are well-documented. From an economics standpoint, surveillance systems impose costs on the entire student population (all students bear the surveillance burden) to address the behavior of a subset — an inefficient targeting of costs. Assessment redesign, by contrast, changes the environment for all students in a way that reduces cheating at no targeting cost.

---

## 7. Vietnam-Specific Economic Analysis

Vietnam's specific context modifies the general analysis in important ways:

**Low-income country credential premium**: In a developing economy context, the private returns to education credentials are high and rising. Vietnam's credential premium creates stronger incentives for AI fraud than exist in high-income countries where on-the-job training provides alternative human capital pathways. This higher benefit-of-fraud component of the cost-benefit calculation means deterrence requires correspondingly higher probabilities of detection and penalties — a standard result from crime economics (Becker 1968 on optimal law enforcement).

**Brain drain interaction**: Vietnam faces significant brain drain among its highest-skilled graduates. If credential inflation from AI fraud degrades the signal value of Vietnamese degrees in international labor markets, the returns to genuine investment in Vietnamese education decline for the most mobile (highest-ability) workers — who are precisely the workers whose retention provides the largest positive externality to Vietnam's economy. AI fraud thus interacts negatively with brain drain: it accelerates departure of genuine talent who see their credential signal contaminated by widespread fraud.

**ESL false positive problem**: As noted, detection tools produce catastrophically high false positive rates for non-native English speakers (Liang et al. 2023). Vietnam's higher education is predominantly Vietnamese-medium, but international programs and English-medium courses are growing under QĐ 1705's internationalization targets. Deploying English-trained detection tools against Vietnamese student writing — the natural temptation as Vietnam's institutions adopt international practices — would create a systematic equity problem. The economic harm falls disproportionately on students from lower-income backgrounds (who are less likely to write English at native-speaker proficiency levels and thus more likely to receive false positive detections).

**Market structure of Vietnamese EdTech**: Vietnam's EdTech market is structurally less developed than Singapore's or South Korea's, creating both a risk and an opportunity. The risk: international EdTech companies selling detection products that are not validated for Vietnamese conditions capture institutional budgets while delivering lower quality outcomes than claimed. The opportunity: Vietnam can adopt more cost-effective assessment redesign approaches (oral defense, process portfolios leveraging Google Workspace) without having sunk costs in detection infrastructure that create switching cost lock-in.

**Policy vacuum between QĐ 1705 and Decree 109/2022**: The coexistence of Vietnam's education strategy (QĐ 1705, which promotes AI adoption without integrity safeguards) and academic integrity regulations (Decree 109/2022, which defines integrity categories without AI provisions) creates a policy gap that functions as an implicit subsidy to AI fraud. When the legal environment is ambiguous, students rationally interpret ambiguity in their favor (i.e., "if it's not explicitly prohibited, it must be permitted"). The economic cost of this ambiguity is estimated by the 3x concealment rate: if students believed enforcement was credible and clearly scoped, concealment rates would be lower — this is standard deterrence theory prediction.

---

## 8. Unacceptable Proposals from an Economic Standpoint

The following policy responses, commonly proposed, fail basic economic efficiency tests:

**"Solve it with better detection tools"**: Fails because of the arms race problem, the ESL false positive equity problem, and the information asymmetry in the detection tool market. More spending on detection with no structural reform is throwing money into an infinite arms race with no stable equilibrium. The correct economic response is to change the game, not to play it more expensively.

**"Trust students to disclose AI use voluntarily"**: Fails because the 3x concealment ratio provides direct empirical evidence that the honor-system-alone approach does not produce honest disclosure under current incentive structures. Self-disclosure requirements have utility as part of a multi-layered system (they create a legal/moral obligation that slightly raises the psychological cost of fraud), but as a primary enforcement mechanism they are demonstrably inadequate.

**"Ban AI tools entirely from university networks"**: Technically infeasible at non-prohibitive cost (students use personal devices and mobile networks), economically counterproductive (prevents legitimate human capital accumulation in AI skills), and legally complex. This is the educational equivalent of Prohibition — it drives the behavior underground while failing to eliminate it, generates evasion costs, and foregoes the potential benefits of regulated use.

**"Penalize institutions rather than students"**: While institutional accountability has theoretical appeal, it creates perverse incentives: institutions would suppress reporting of detected cases to avoid reputational penalties, making the problem less visible rather than less prevalent. This is the classic measurement teaching-to-the-test problem in institutional accountability design (Hanushek & Raymond 2005).

---

## 9. Optimal Policy Package: Economic Rationale

An economically optimal policy package for Vietnam should:

**Tier 1 — Eliminate the arms race game board through assessment redesign mandate**
MOET should issue a circular under QĐ 1705's authority requiring all institutions to implement AI-resistant assessment mechanisms (oral components, process documentation, or in-person production) for a minimum percentage of summative assessment — say 30% by 2026, 60% by 2028. This converts the problem from one of detection (high cost, arms race, equity problem) to one of design (one-time investment, durable solution). The BUV AIAS framework provides a ready-made operational implementation that is already validated in Vietnamese institutional context.

**Tier 2 — Recalibrate the incentive calculation through nationally standardized penalties**
The current variation in penalty severity (50% grade deduction at HCMUFA versus zero-marks at NTU Singapore) creates an arbitrage opportunity for students at more lenient institutions. A nationally standardized tiered penalty schedule — warning for first low-stakes offense, zero assignment for moderate fraud, course failure for severe or repeat fraud — would standardize the cost-of-fraud term in the student's expected value calculation and reduce penalty arbitrage. This requires a MOET Circular supplementing Decree 109/2022.

**Tier 3 — Invest in honor code culture as the long-run efficiency solution**
McCabe's empirical finding that honor code institutions show 25-30% lower cheating rates is the strongest evidence for a high-ROI long-run investment. The payback period is long (culture change takes years), but the steady-state efficiency gain — eliminating the need for expensive detection infrastructure — is substantial. Vietnam should include honor code culture development in QĐ 1705's teacher development and institutional governance provisions.

**Tier 4 — Resolve the detection market failure through regulation, not procurement**
If detection tools are to be used, require that any detection tool deployed by Vietnamese institutions meet validated accuracy standards (maximum false positive rate for Vietnamese-language and Vietnamese-English-medium writing, independently audited). This shifts the information asymmetry burden from institutions (who currently cannot evaluate tool quality) to vendors (who must demonstrate performance). Comparable to pharmaceutical efficacy standards — you must prove your product works before selling it into a vulnerable market.

**Tier 5 — Advocate for LLM watermarking through ASEAN governance channels**
The collective action problem blocking LLM watermarking deployment requires multilateral coordination. Vietnam's participation in ASEAN AI governance forums should include explicit advocacy for mandatory watermarking — consistent with China's existing AI-generated content labeling requirements (Cyberspace Administration 2023) and the EU AI Act Article 50 direction. This is a low-cost intervention for Vietnam with potentially high long-run returns if regional watermarking standards are achieved.

---

## 10. Conclusion

The academic integrity crisis created by generative AI is, at its core, a market failure problem: signal degradation through adverse selection, negative externalities from credential inflation, and a prisoners' dilemma arms race between detection and evasion. Individual moral exhortation cannot solve structural market failures; only institutional design can.

The economically rational response is not to invest more in the losing side of an arms race. It is to redesign assessments that make AI substitution structurally impossible, standardize deterrence through nationally consistent penalties, build the long-run cultural capital that makes integrity self-enforcing, and advocate internationally for the technical solutions (LLM watermarking) that can eventually make detection both reliable and non-discriminatory.

Vietnam faces this challenge with a specific vulnerability — a high credential premium, a developing detection infrastructure, and an ESL false positive problem that makes detection tools particularly harmful — and a specific opportunity: the country can learn from expensive mistakes made by early-adopting Western institutions and build its AI integrity infrastructure on first-principles economic analysis rather than reflexive surveillance escalation.

The optimal policy is not the most expensive policy. It is the policy that correctly identifies where the market has failed and applies the right corrective mechanism at each failure point.

---

## Key Data Points Referenced

| Datum | Source |
|---|---|
| AI cheating 3x self-reported rate in Vietnam | Springer 2024, N=1,386 Vietnamese undergraduates |
| Sheffield AI misconduct cases: 6 → 92 (15x increase) | Times Higher Education FOI data, 2024 |
| GPTZero false positive rate on TOEFL essays: 61.3% | Liang et al., Stanford HAI / PLOS ONE, 2023 |
| Turnitin AI claimed accuracy 98%, WaPo testing ~50% | Washington Post independent evaluation, 2023 |
| Contract cheating self-report rate: 15.7% globally | Newton 2018, Frontiers in Education systematic review |
| Springer Nature 2024 retractions: 2,923 (record) | Retraction Watch, February 2025 |
| NeurIPS 2025: 100+ hallucinated citations in 51 papers | GPTZero Report, January 2026 |
| Honor code institutions: 25-30% lower cheating rates | McCabe, 70,000+ student longitudinal survey |
| HCMUFA penalty: 50% deduction (first Vietnamese AI fraud case) | VietnamNet 2023 |
| OpenAI watermarking built but not deployed (competitive disadvantage) | Aaronson blog post, August 2023 |
| ChatGPT passes medical school assessments | Newton & Xiromeriti 2023, Computers & Education |

---

*This position paper was prepared for the Buổi 5 debate on academic integrity and AI fraud in EdTech research, Nhập môn KHGD, HCMUS, Semester 2 2025-2026.*
