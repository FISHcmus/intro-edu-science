# Debate Supplement: Corrected Rebuttals, Strawman Corrections, and Revised Analysis

*Supplement to final_report.md. Prepared post-debate, incorporating critical_gaps.md analysis and three new position papers.*

---

## Part 1: Corrected Strawmanning

### 1.1 The CUHK Misrepresentation

Throughout the debate transcript and final_report.md, CUHK's academic integrity policy was used as the canonical example of bad zero-tolerance policy. In Round 4, LW stated: "potential expulsion" as if expulsion for AI fraud were CUHK's standard penalty; in the final report's Section 5.2, CUHK is cited as the paradigm case for "blanket AI prohibition policies" rejected across the board. The final report's Recommendation 8 explicitly positions Vietnam's proposed national penalty schedule as a correction to the "CUHK (potential expulsion)" end of the spectrum.

**The actual CUHK policy**: CUHK employs a graduated penalty structure in which expulsion is the maximum sanction reserved for severe cases — most commonly repeat offenses or large-scale organized fraud — not the default or first-offense response. First offenses in written coursework typically draw failing grades for the assignment or course, not expulsion. The policy architecture resembles the tiered schedule the debate itself recommends for Vietnam.

**What this correction does to the debate**: Three specific claims are weakened:

1. The final report's Section 5.2 rejection of "blanket AI prohibition policies (CUHK model)" rests substantially on the mischaracterization. If CUHK's model is tiered and proportionate, it is much closer to the "tiered national schedule" the report recommends in Section 4, Recommendation 8 than the report acknowledges. The binary opposition of "bad CUHK policy" versus "good tiered schedule" partly collapses.

2. Round 2's LW argument — "disproportionate enforcement falls on students without social capital to navigate appeals" — cited the threat of expulsion as the mechanism. If expulsion is reserved for severe cases with meaningful procedural protection, this claim requires qualification; it remains valid as a general institutional power asymmetry argument but the CUHK example no longer supports it as stated.

3. The Technologist's endorsement of "functionally not implemented" blanket prohibition (Round 2, Rebuttals) referenced CUHK as the paradigm. If CUHK does not actually practice what the debate attributed to it, the debate's taxonomy of "blanket prohibitions that fail" versus "tiered contextual frameworks that work" is using a mislabeled example. This does not change the underlying policy conclusion — blanket prohibition is genuinely worse than tiered frameworks — but it means the debate's strongest case study for that claim must be replaced with an accurate one.

---

### 1.2 Liang et al. (2023) Overgeneralization

The final_report.md treats the Liang et al. 61.3% false positive finding as definitively applicable to Vietnamese students throughout. It appears in Section 1.3 as the cornerstone of the detection consensus, in Section 3.3 (ESL students as rights-bearers), in Section 4 Recommendations 5 and 10, and it is cited in the debate transcript in every round. The debate moderator noted it as "empirically binding by the entire panel" (Round 2 moderator assessment).

**The scope problem**: Liang et al. tested TOEFL essays. This matters for three reasons:

First, TOEFL essays are English-medium by definition, written by test-takers preparing for Anglophone academic contexts. This is a population selected for English proficiency aspiration, writing in a constrained high-stakes format under timed conditions, producing formulaic five-paragraph structures aligned with TOEFL scoring rubrics. The stylistic features that produce high false positive rates — low lexical diversity, formulaic transitions, compressed sentence variety — are features of TOEFL essay genre, not features of ESL writing in general.

Second, Vietnamese students writing in Vietnamese-medium instruction are not in this Liang et al. sample at all. The detection tools being evaluated use perplexity models trained on English corpora. Their behavior on Vietnamese-language text is not measured by Liang et al. — the tools may fail entirely differently (false negative, inability to classify, or different false positive patterns) on Vietnamese-medium submissions.

Third, Vietnamese students using AI in Vietnamese and then translating — a realistic fraud pathway under Vietnam's expanding English-medium instruction — produce text with a different statistical signature than both native-speaker English and TOEFL essay ESL English. Whether the 61.3% figure overstates or understates the risk for this pathway is empirically unanswered.

**Round 2 and Round 4 arguments requiring qualification**:

- LW's Round 2 argument ("Vietnamese ESL writers face 40-fold false positive disparity") extrapolates from Liang et al.'s Chinese-college-TOEFL-essay population to Vietnamese students as if the populations were equivalent. The mechanism is plausible; the magnitude requires direct validation.
- LW's Round 4 specific recommendation (explicit MOET prohibition of tools trained on native-English corpora) rests on the 61.3% figure as its empirical basis. If that figure is not directly applicable to Vietnamese-medium instruction, the prohibition's most urgent justification — harm occurring now in Vietnamese proceedings — requires qualification. The prohibition may still be justified on precautionary grounds, but the evidence it is preventing documented harm to Vietnamese students specifically (rather than harm documented against Chinese TOEFL test-takers) has not been established.
- The final report's Open Question 1 (Section 6) correctly identifies this gap but does not adjust its confidence level in the detection consensus accordingly. The consensus is stated more firmly than the evidence warrants.

---

### 1.3 McCabe Honor Code Findings — Cultural Transferability

The final_report.md elevates McCabe's 25-30% cheating reduction finding to Claim 1.8 — "the Most Important Single Datum in the Long-Run Literature" — with a note that "all participants accept this finding." The debate treats it as a universal effect size applicable to institutional interventions in Vietnam (Round 3, ED's endorsement; Round 4, CT's synthesis).

**The institutional specificity problem**: McCabe's primary dataset comes from institutions with particular histories. West Point has a century-long honor code tradition enforced by peer reporting and expulsion for first offense. University of Virginia's honor code dates to 1842 and is student-administered with student-controlled expulsion proceedings. Rice University's honor code includes unproctored examinations specifically because the honor code is the exam's enforcement mechanism. These are not typical universities — they are institutions selected partly because students who attend them accept the honor code as a condition of enrollment. The selection effect is not a minor methodological footnote; it may account for a substantial portion of the 25-30% effect size.

**Claims in the debate requiring qualification**:

- ED's Round 3 argument — "oral defense is the only intervention with an effect size larger than honor code culture" — assumes McCabe's 25-30% figure is achievable in contexts without West Point's institutional history. In Vietnamese universities where student-administered honor code culture does not exist as a tradition, where the faculty-student power differential makes peer reporting socially hazardous, and where grade competition in credential-premium contexts incentivizes individual rather than collective integrity norms, the replication of McCabe's effect size cannot be assumed.
- The final report's Long-Term Recommendation 14 ("Honor code culture development as a multi-year institutional investment" with reference to McCabe's 25-30%) should qualify that this effect size was documented in US institutions with specific self-selection properties, and that cross-cultural validity studies are absent. Open Question 6 in Section 6 of the final report acknowledges this but the Recommendation 14 text does not hedge its claim accordingly.
- Critical_gaps.md Section 5.2 explicitly calls for a cross-cultural validity study of McCabe's findings in Vietnamese, Chinese, and Indian contexts. This study does not exist. Treating the finding as universal in the meantime is methodologically appropriate for a prior in the absence of disconfirmation, but the confidence level in Claim 1.8 should be stated as conditional: "if McCabe's findings transfer to Vietnamese institutional contexts."

---

## Part 2: Missed Rebuttals — What Should Have Been Said

### 2.1 Round 2: The Liang et al. Scope Problem

*The rebuttal that should have been delivered, as if by the Technologist or Economist challenging LW's use of Liang et al.:*

> LW, you have been treating Liang et al. as if it directly measures the risk to Vietnamese students in Vietnamese universities. It does not. Read the paper. The subjects are TOEFL essay writers — Chinese college students writing English under TOEFL test conditions. TOEFL essays are structurally formulaic: five paragraphs, constrained vocabulary, timed production that penalizes risk-taking in word choice. These students were not writing graduate seminars or disciplinary research essays. They were writing to a rubric designed to measure basic English-medium academic communication, in a format that produces text optimized for scoring criteria, not for stylistic richness.
>
> The detection tools flag their writing as AI-generated because TOEFL essay style has low perplexity and low burstiness — the same statistical signatures as GPT output. But that is a feature of TOEFL essay genre, not a universal feature of all ESL academic writing. A Vietnamese student writing a social science analysis in Vietnamese does not produce text with TOEFL essay statistical signatures. A Vietnamese student writing an English-medium management essay at a Western-affiliated institution may — or may not — depending on their proficiency level, the assignment format, and whether they have been taught to write in TOEFL-adjacent styles.
>
> My point is not that Vietnamese students face no false positive risk. My point is that the 61.3% figure cannot be transplanted from TOEFL essays to Vietnamese university contexts without a validation study that does not exist. Your policy prescription — a blanket prohibition — may be the right answer. But its empirical foundation is an inference, not a measurement. We should be honest about that distinction when we are proposing MOET-level regulation affecting 2.1 million students.

---

### 2.2 Round 3: The Game Theory of 10% Sampling

*The rebuttal that should have been delivered, as if by the Left-Wing or Technologist challenging the Economist's deterrence math:*

> EC, your NPV calculation for spot vivas looks correct on the input numbers. Ten hours per 300-student cohort. Positive NPV versus detection tool costs. But your deterrence logic has a game theory problem you have not addressed, and it matters for whether the "10% sampling deters fraud" claim holds.
>
> If 10% of submissions are sampled for viva, and students learn this sampling rate — which they will, because sampling rates are either published in course policy or inferred within one semester through peer network information — then the expected cost of AI fraud remains calculable. A student using AI has a 90% chance of never being called for a viva. The expected penalty is 0.1 multiplied by the penalty for discovery. If the penalty for discovery in a viva context is a failing grade for the assignment, the expected penalty is 0.1 times whatever percentage the assignment represents. For a 20% assignment, the expected penalty is 2 percentage points of final grade. In Vietnam's credential premium context, where the benefit of a clean submission (full marks) on a 20% assignment is 20 percentage points of final grade, the rational calculation of AI fraud remains substantially positive-expected-value at 10% sampling.
>
> For the deterrence to actually work, either the sampling rate needs to be high enough to make the expected penalty exceed the expected benefit — probably 40-50% for typical assignment weights in Vietnam's grade-competitive environment — or the penalty conditional on viva discovery needs to be severe enough to compensate for the low probability of being sampled. Your framework does not establish which of these conditions holds. If institutions announce 10% sampling but rely on discovered students self-regulating out of moral conviction, that is honor code theory, not deterrence theory. Pick your model.

*The Economist's counter-rebuttal:*

> You are correct on the expected value math for a fully informed rational actor in a one-shot game. But deterrence does not require that every rational actor abstain — it requires that fraud rates fall to levels where the remaining fraud does not significantly degrade credential quality. The Akerlof lemons dynamic requires widespread fraud to produce market collapse; it tolerates some fraud without catastrophic signal degradation.
>
> Moreover, your model assumes students know the sampling rate and compute expected value correctly. Behavioral economics is clear that humans are poor at probability assessment for low-frequency events. The psychological effect of knowing that a viva is possible — the salience effect — produces risk-aversion beyond what the objective probability warrants. Kahneman and Tversky's prospect theory predicts that students will overweight the possibility of being called for a viva relative to the objective 10% probability, which is precisely the deterrence mechanism that makes sampling-based approaches more effective than the expected value calculation implies. Finally, institutional signaling matters: institutions that implement viva sampling communicate seriousness of purpose, which shifts the perceived social norm around AI fraud independent of the mathematical deterrence calculation.

---

### 2.3 Round 4: The Vietnamese-Language Detection Gap

*The rebuttal from the Center or Educator that should have been delivered:*

> LW, your Round 4 proposal to prohibit AI detection tools trained on native-English corpora from use in Vietnamese proceedings is the most concrete recommendation of this round, and I want to support it — but I want to ask you the question that follows from it and that you have not answered.
>
> If we prohibit detection tools trained on native-English corpora, what tools are permissible? Are there AI detection tools trained on Vietnamese-language academic writing? If the answer is no — and I believe it is no, because the Vietnamese-language NLP detection ecosystem does not have the institutional infrastructure that produced GPTZero or Turnitin — then your prohibition effectively eliminates all AI detection from Vietnamese academic proceedings. That may be the right outcome. But you should say so explicitly, because "prohibit biased tools" and "prohibit all detection tools" have different policy implications and different political economy implications for how MOET would receive the proposal.
>
> If Vietnamese-language detection tools do not exist, that is also a research funding question, not merely a policy question: should Vietnam invest in developing detection tools validated on Vietnamese student writing corpora, or should it invest that same money in assessment redesign infrastructure? These are not the same investment. I need you to tell us whether your prohibition is a transitional prohibition pending development of validated tools, or a permanent prohibition based on the view that AI detection is never an acceptable enforcement instrument.

*LW's response:*

> Fair challenge. My position is a permanent prohibition on detection tools as standalone enforcement evidence, not a transitional prohibition pending better tools. The reason is principled, not just empirical: even a Vietnamese-language detection tool validated to low false positive rates does not resolve the due process problem — any detector that assigns probabilistic guilt to individual students based on statistical text properties has an irreducible error rate that produces wrongful accusations. The question of what evidence standard is appropriate for academic misconduct proceedings should not be resolved by "find a detector with lower false positive rates." It should be resolved by asking whether statistical text analysis ever meets the evidence standard that academic misconduct proceedings require. My answer is no. The tool that is permissible is a competent human examiner — not a detector of any kind — which is why oral defense is the correct institutional investment regardless of whether Vietnamese-language detection tools are developed.

---

### 2.4 Throughout: The McCabe Cultural Specificity Challenge

*A composite challenge, as if from a Vietnamese scholar or the Right-Wing position:*

> The McCabe honor code finding — 25-30% lower cheating rates in honor code institutions — has been cited in this debate as if it were a universal finding with direct applicability to Vietnamese universities. I want to challenge that assumption directly.
>
> Vietnam's educational culture is Confucian-influenced, hierarchical, and collectivist in ways that make the peer-enforcement mechanisms underlying US honor codes politically and socially difficult to replicate. US honor code culture, particularly at its strongest institutions — West Point, UVA, Rice — depends on students reporting other students for violations. The institutional culture treats peer reporting as a civic duty. In Vietnam's educational culture, where face-saving norms and collective solidarity between classmates create strong social sanctions against reporting, peer enforcement is not a readily available mechanism. Students who report a classmate for AI fraud in a Vietnamese university face social costs that US honor code students at West Point do not.
>
> Additionally, McCabe's sampling is not random. The institutions he studied in depth are self-selected: they are institutions where honor code culture already exists and where students chose to enroll partly because of that culture. This selection effect means his 25-30% finding may reflect the combination of culture plus selection, not culture alone. If you build an honor code from scratch in a Vietnamese institution without selection effects, you are not guaranteed to achieve McCabe's effect size.
>
> This does not mean honor code culture is useless in Vietnam. Vietnam has its own traditions of collective responsibility for community standards — it may be possible to build genuine integrity culture through mechanisms that are culturally appropriate rather than importing US peer-reporting models. But those mechanisms need to be designed for Vietnam, not transplanted from West Point, and the effect size should be treated as an upper bound pending Vietnamese-context evidence.

*The response from the Educator:*

> The cultural specificity challenge is correct and important. But I want to note that the challenge cuts in an unexpected direction for Vietnam. McCabe's finding rests on student ownership of integrity values — students who treat integrity as a community good rather than a compliance obligation. Vietnamese Confucian educational traditions actually have a version of this: the concept of liêm sỉ — moral shame as a collective social sanction — operates through different mechanisms than US peer reporting but serves analogous functions. The challenge for Vietnam is not that honor code culture is foreign to Confucian traditions; it is that Vietnam's contemporary university system has largely displaced both Confucian moral culture and Western honor code culture with a bureaucratic compliance framework. Building genuine integrity culture means recovering something, not importing something. The mechanism differs; the goal is recognizable within Vietnamese tradition.

---

## Part 3: How the Three New Papers Change the Consensus

### 3.1 Claims That Survive Nine-Position Scrutiny

The following consensus claims from final_report.md hold under challenge from Adaptive Minimalism (Position 7), AI Industry (Position 8), and Professional Licensing (Position 9):

**Claim 1.3 (AI Detector Output Cannot Serve as Sole Evidence)** survives intact. Adaptive Minimalism explicitly accepts this: "clear guidance that detection tool output is probabilistic, not evidential" appears in its Section 7 accepted interventions. Professional Licensing concedes the false positive problem while arguing for targeted proctoring in licensing contexts — it does not argue for detection tools as sole evidence. The AI Industry position, reasoning from OpenAI's own stated guidelines that warned against "sole reliance" on its detection tools before OpenAI discontinued its own detection product, would not contest this claim.

**Claim 1.4 (Assessment Redesign as Highest-Priority Intervention)** survives with strengthening. Adaptive Minimalism endorses oral examination and portfolio components "where pedagogically motivated" and explicitly states that the Educator paper's assessment redesign outcomes are endorsed even while rejecting the institutional machinery. Professional Licensing positions oral defense and process documentation as its central mechanism for high-stakes contexts. AI Industry papers from OpenAI's educational deployment documents consistently recommend "process-based assessment that cannot be replicated by AI submission alone."

**Claim 1.7 (AI Literacy as Prerequisite)** survives unanimously. Adaptive Minimalism's Section 7 accepts "institutional AI use policies that are clear, contextually differentiated, and published transparently." No new position contests this.

---

### 3.2 Claims That Require Revision

**Claim 1.2: "AI Fraud Is Primarily a Structural Problem, Not an Individual Moral Failure"**

Adaptive Minimalism challenges the word "primarily" through a different route than the right-wing paper's "individual responsibility" argument. The Adaptive Minimalist challenge is evidentiary: the claim assumes that structural factors are causing a significant net increase in academic dishonesty. But as Position 7 argues in Section 3, the base-rate comparison has not been made — there is no pre-ChatGPT baseline using identical methodology to establish that total academic dishonesty (AI plus essay mills plus traditional cheating) has increased structurally rather than merely shifted form. If students substituting AI fraud for essay mill fraud represent no net increase in dishonesty, the "primarily structural" diagnosis is not wrong, but the urgency it implies — that structural failures are producing measurably worse outcomes — is not established.

**Revised formulation**: "AI fraud is embedded in structural incentive failures documented before AI's emergence; the extent to which AI has increased total academic dishonesty beyond these pre-existing structural baselines has not been established."

**Claim 1.6: "LLM Watermarking Is the Correct Long-Term Technical Solution"**

The AI Industry position (reasoning from the companies' own published rationales) significantly complicates this claim. The debate correctly identified watermarking as a collective action problem. But the AI Industry analysis reveals a deeper structural reason why collective action is unlikely: the companies most capable of deploying effective watermarking have commercial interests in not deploying it that extend beyond competitive disadvantage between commercial players. Meta's open-source philosophy — releasing Llama weights without API restrictions — is not merely a competitive strategy; it reflects a stated principle that open-source AI benefits should be broadly accessible, which is in direct conflict with watermarking mandates that require proprietary access control. A watermarking regime that covers commercial API calls but not open-source model weights (the Technologist's concern in Round 3) is not a "correct long-term solution" — it is a solution that applies to the minority of AI use cases that are commercially mediated while the majority of sophisticated use (including the most likely student fraud pathways by 2028) escapes it entirely.

**Revised formulation**: "Cryptographic watermarking of commercial LLM outputs is technically sound but will cover a diminishing fraction of actual AI use as open-source models proliferate; it is a partial mitigation, not a comprehensive solution."

**The Surveillance Rejection — Professional Licensing Carve-Out**

The final_report.md Rejected Proposal 3 states: "Continuous keystroke monitoring, biometric proctoring, and surveillance-as-integrity infrastructure" — rejected unanimously. Professional Licensing (Position 9) carves out a justified exception that the debate did not engage with. For medical board examinations, bar examinations, and engineering licensing, the argument is: the expected harm from a fraudulently certified physician is not the credential inflation harm that primarily concerns the debate's analyses — it is direct patient harm, an asymmetry that changes the acceptable false positive tolerance and the acceptable surveillance depth.

The Adaptive Minimalism paper's Section 6 concedes this: "professional licensing contexts — medical board examinations, bar examinations, engineering licensing, pilot certification — are categorically different and warrant stricter controls." This convergence between Adaptive Minimalism and Professional Licensing on the licensing exception is notable because these are the two positions most likely to disagree on everything else.

**Required revision to final_report.md Section 5.3**: Add language distinguishing mass undergraduate surveillance (rejected unanimously and correctly) from targeted process-based monitoring in professional licensing credentialing contexts (justified where patient or public safety is at stake, subject to proportionality and due process requirements). The current language conflates these without distinction.

---

### 3.3 New Points of Irresolvable Disagreement

Nine-position analysis reveals two genuinely irresolvable disputes that were obscured when only six positions were present:

**Irresolvable Dispute A: Whether the AI fraud crisis crosses the base-rate threshold for emergency intervention.**

Adaptive Minimalism and the original six positions disagree on a question that cannot be resolved by additional evidence unless a specific study design is accepted. The dispute is: should the counterfactual baseline for measuring AI fraud's impact be (a) pre-ChatGPT academic dishonesty rates, in which case the question is whether total dishonesty has increased, or (b) the pre-ChatGPT assessment environment, in which case any measurable AI fraud represents a new policy problem requiring response even if total dishonesty is stable?

This is not merely a values question about risk tolerance. It is a disagreement about what causally requires institutional response — a normative question about policy triggers that cannot be settled by data on fraud prevalence, because the disagreement is about which data is relevant to the policy question. Adaptive Minimalism would require a demonstrated causal increase in total dishonesty. The original six positions require only demonstrated AI fraud prevalence. No evidence could settle this dispute because the parties have different implicit theories of what makes a policy problem policy-actionable.

**Irresolvable Dispute B: Whether surveillance infrastructure for academic integrity is categorically distinguishable from general population surveillance infrastructure in Vietnam's political context.**

Adaptive Minimalism's Section 5 raises the authoritarian reuse concern — that behavioral monitoring infrastructure built for academic integrity has non-educational reuse potential in Vietnam's political environment. This concern cannot be resolved by evidence about academic integrity policy design, because it is a claim about the political behavior of state actors under conditions of institutional opportunity. The original six positions implicitly assumed that surveillance infrastructure would be controlled by its stated purpose; Adaptive Minimalism denies that assumption on the basis of Vietnam's regulatory history. No study of academic integrity policy design can settle a dispute about how surveillance infrastructure will be appropriated by state actors over time.

---

### 3.4 Revised Policy Recommendations

**Additions required**:

1. Explicitly distinguish mass undergraduate AI monitoring from targeted professional licensing verification. Add to Section 4 a sub-recommendation under Immediate Actions: "For professional licensing bodies (medical, legal, engineering) operating within Vietnam's regulatory framework, process-based verification — portfolio documentation, supervised practical examination, structured oral defense — is appropriate and proportionate. This is not an exception to the surveillance rejection; it is the application of the consensus's preferred assessment redesign methodology to the highest-stakes contexts."

2. Add a recommendation specifically addressing surveillance infrastructure lock-in, drawing from Adaptive Minimalism's Section 5: "Vietnamese institutions evaluating AI integrity infrastructure should explicitly assess authoritarian reuse potential in any monitoring system that creates behavioral profiles of students. Any system logging writing process data, browser activity, or keystroke dynamics creates profiles whose downstream use cannot be controlled by academic integrity policy alone."

**Modifications required**:

3. Recommendation 8 (standardize national penalty schedules, citing CUHK as one pole) should correct the CUHK characterization per Part 1.1 above: CUHK's graduated schedule is cited as an example of excessive zero-tolerance policy, but CUHK's actual policy is tiered. The recommendation stands; the example should be replaced with the HCMUFA 50% deduction as the underpenalty pole and specific jurisdictions with documented expulsion-for-first-offense policies as the overpenalty pole.

4. Recommendation 12 (international regulatory coordination for LLM watermarking) should add: "Watermarking coordination should explicitly include open-source model governance, or it will cover only commercially-mediated AI use while leaving the primary fraud pathway — locally-run open-source models — unaddressed. Vietnam's advocacy in ASEAN AI governance forums should push for open-source model governance as part of any watermarking mandate, recognizing that Meta and other open-source AI actors are not party to commercial API regulatory frameworks."

**Scoping modification**:

5. Claim 1.6's policy implication — that advocating for LLM watermarking is a "low-cost advocacy position with potentially high long-run returns" (Section 4, Recommendation 12) — should be scoped to: "low-cost advocacy position with potentially high returns for commercial API-mediated AI use, but diminishing returns as open-source model proliferation advances."

---

## Part 4: Remaining Gaps

After nine position papers, four debate rounds, and this supplementary analysis, the following gaps remain genuinely open:

**What a tenth position paper would cover — Vietnamese Frontline Faculty Perspective**: None of the nine positions has been written from the perspective of a Vietnamese lecturer at a public university teaching 350 students per cohort with no teaching assistant, no institutional AI policy guidance, and salary pressure that makes additional oral defense time disproportionately costly. This perspective would interrogate every consensus recommendation on the basis of practical implementability in under-resourced Vietnamese public HE contexts. The Educator paper (Position 6) reads as a Western learning scientist; it does not confront the actual material conditions of Vietnamese public university teaching.

**What an eleventh position paper would cover — Vietnamese Student Voice**: The entire corpus discusses students as policy objects. No position paper presents authentic student perspectives on: being falsely accused of AI fraud, using AI for legitimate learning acceleration while navigating unclear institutional policies, or the decision-making process that produces AI-assisted submissions. The Springer 2024 Vietnamese study (N=1,386) measures prevalence but not motivation, perceived fairness, or policy preferences. A position paper written from student research or student testimony would be the most disruptive addition to the existing framework.

**Research questions that remain genuinely unanswered**:

1. What is the actual false positive rate for AI detection tools applied to Vietnamese-medium student writing? The debate assumes the Liang et al. figure applies; it does not.

2. Does the McCabe honor code effect size replicate in Vietnamese educational contexts? The debate treats it as universal; the cultural specificity challenge in Part 2.4 above is not resolved by existing research.

3. What is the total academic dishonesty rate — AI plus essay mills plus traditional cheating — compared to pre-2022 baselines using equivalent methodology? The Adaptive Minimalism challenge on base rates (Section 3 of position_adaptive_minimalism.md) cannot be answered without this study.

4. What is the interaction between tự chủ đại học performance incentives and AI fraud prevalence? The RW-LW convergence in Round 4 identified this as a concern; it remains empirically unstudied in the Vietnamese context.

5. Can surveillance infrastructure built for academic integrity be adequately protected against authoritarian reuse in Vietnam's regulatory environment? This question may not be answerable empirically; it requires constitutional and administrative law analysis of Vietnam's institutional accountability mechanisms.

---

*Supplement prepared for Nhập môn Khoa học Giáo dục (25CGD), HCMUS, Semester 2 2025-2026.*
*Supplements: final_report.md, debate_transcript.md, critical_gaps.md, position_adaptive_minimalism.md.*
*Additional positions referenced: AI Industry (Position 8, forthcoming), Professional Licensing (Position 9, forthcoming).*
