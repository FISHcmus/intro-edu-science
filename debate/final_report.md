# Final Synthesis Report: Academic Integrity and AI Fraud in EdTech

**Participants synthesized:**
- Right-Wing Analyst (RW) — Heritage/AEI free-market tradition
- Left-Wing Activist (LW) — Critical EdTech, Selwyn tradition
- Center Technocrat (CT) — Brookings/OECD evidence-based pragmatism
- Economist (EC) — Becker/Spence/Akerlof education economics
- Educator (ED) — Learning science, Gallant/McCabe/Luckin tradition
- Technologist (TE) — ML systems, detection theory (arXiv:2301.10226)

---

## 1. The Consensus Zone

These propositions are accepted by all or virtually all participants, despite major ideological differences. They constitute the empirically grounded foundation for any serious policy response.

### 1.1 The Problem Is Real and Documented at Scale

Every participant accepts that AI academic fraud is a genuine crisis, not a moral panic. Key agreed facts:

- University of Sheffield: 6 confirmed AI misconduct cases (2022-23) to 92 (2023-24), a 15x increase
- Springer 2024 Vietnamese study (N=1,386): actual AI fraud rate is approximately 3x the self-reported rate
- Hindawi/Wiley: 8,000+ papers retracted in 2023, ~80% of all global retractions that year, $35-40M in losses
- Springer Nature: 2,923 retractions in 2024, a single-publisher annual record
- NeurIPS 2025: 100+ hallucinated citations across 51 accepted papers, detected by zero peer reviewers

No participant denies these figures. The problem is structural, not marginal.

### 1.2 AI Fraud Is Primarily a Structural Problem, Not an Individual Moral Failure

McCabe, Butterfield, and Treviño's survey of 70,000 US college students found approximately two-thirds self-reporting at least one instance of dishonesty — *before* AI. Gallant (2008) established that academic dishonesty is a systemic symptom of institutional failure. Every participant accepts this framing. When two-thirds of students cheat, the barrel is broken, not the apples.

This consensus does not eliminate individual responsibility. It locates that responsibility correctly within a larger structure of institutional incentives.

### 1.3 AI Detector Output Cannot Serve as Sole Evidence in Disciplinary Proceedings

The Liang et al. (Stanford, 2023, *Patterns*) finding — 61.3% false positive rate for ESL writers versus 1.5% for native English speakers — is accepted by RW, LW, CT, EC, ED, and TE as disqualifying AI detection tools from standalone enforcement use. This includes ideologically opposed participants RW and LW. Turnitin's claimed 98% accuracy versus independent testing at approximately 50% compounds the problem. The Technologist confirms the mechanism: perplexity-based detection systematically misclassifies non-native English proficiency as AI authorship because both produce similar low-perplexity, low-burstiness text signatures.

Proposition: **No grade penalty, academic sanction, or misconduct finding should be based solely on AI detector output.** This is a consensus red line.

### 1.4 Assessment Redesign Is the Highest-Priority Intervention

Oral defense (spot viva), process-based staged submissions, and contextually situated assessments are endorsed by all six participants. The reasons differ by perspective:

- ED: Pedagogically sound independent of fraud concerns; measures genuine learning
- TE: Technologically robust — oral defense is not undermined by GPT-5 or open-source model proliferation
- EC: Economically efficient — positive NPV versus detection tool costs; eliminates arms race game board
- CT: Operationally validated by BUV's AIAS pilot in Vietnamese institutional context
- RW: Market-consistent — creates institutional competitive differentiation based on assessment quality
- LW: Equitable — no false positive rate, no ESL bias, no corporate data extraction

### 1.5 The Detection Arms Race Has No Stable Equilibrium

All participants accept that the detection-evasion cycle (detection tools improve → humanization tools emerge → evasion becomes trivial → detection updates → repeat) is structurally unfavorable to detection. Liang et al. showed that a simple "elevate the writing" prompt defeats detection at greater than 90% success. Commercial humanization tools (Undetectable.ai, QuillBot, HIX.AI) are explicitly trained to evade GPTZero and Turnitin. No participant argues that investing primarily in detection is the right approach.

### 1.6 LLM Watermarking Is the Correct Long-Term Technical Solution, But Cannot Be Deployed Unilaterally

Kirchenbauer et al.'s green/red token scheme (arXiv:2301.10226, ICML 2023) and Aaronson's Gumbel softmax scheme are technically sound. Aaronson built a functional system for OpenAI; OpenAI did not deploy it due to competitive disadvantage if watermarking applies only to their outputs. This is a collective action problem requiring regulatory coordination — accepted by all participants. No participant argues that the technology is inadequate; all agree the barrier is governance, not engineering.

### 1.7 AI Literacy Is a Prerequisite for AI Integrity Policy

No enforcement action against students is legitimate when those students have not been taught what is prohibited and why. All participants accept that AI literacy education — covering what LLMs do, where they fail, institutional policies, and attribution norms — must precede enforcement. This is simultaneously a Bretag "Support" element, an EU AI Act Article 4 requirement, and basic procedural justice. The sequence is non-negotiable: policy publication, then education, then enforcement.

### 1.8 McCabe's Honor Code Finding Is the Most Important Single Datum in the Long-Run Literature

Institutions with genuine honor code cultures show 25-30% lower cheating rates than comparable institutions without such cultures. This effect size is larger than any technical intervention. It operates through changed student motivation, not through changed enforcement. All participants accept this finding, even if they differ on how much weight to give cultural investment relative to other levers.

---

## 2. The Contested Zone

These are issues where reasonable participants genuinely disagree. For each, the best argument for each side is presented, followed by why the disagreement cannot be resolved by evidence alone.

### 2.1 Can Institutional Procedures Neutralize AI Detection Bias?

**The disagreement:** CT and RW argue that AI detection tools used as soft advisory signals, with human review before any penalty, are acceptable policy instruments. LW and ED argue that the human review layer is itself compromised by the same biases the tools encode, and that the Texas A&M failure demonstrates that institutional procedures cannot reliably contain the discriminatory harm.

**Best argument for CT/RW:** The University of Sheffield's 92 confirmed cases and University of Minnesota's 188 cases were handled through multi-signal review procedures. The Texas A&M case was a failure of institutional competence (no training, no protocol, no Turnitin — Mumm used ChatGPT itself), not a failure of detection tools per se. Properly designed procedures, with trained reviewers, bias-aware protocols, and meaningful appeals, can deploy detection tools without reproducing the Texas A&M failure.

**Best argument for LW/ED:** The "human in the loop" relies on institutional competence that is not uniformly present. Most instructors receiving a detection flag have no training in Liang et al.'s findings, no knowledge of ESL false positive patterns, and work within institutional cultures that treat detection flags as presumptive evidence rather than starting hypotheses. The power asymmetry between instructor-as-investigator and student-as-accused is structural, not procedural. Procedures are only as equitable as the training and culture of the humans implementing them.

**Why this cannot be resolved by evidence alone:** This is partly an empirical question about institutional competence — which institutions have procedures adequate to contain the discriminatory harm. But it is fundamentally a values question about whether the risk of institutional discrimination is acceptable in exchange for the benefit of detection-assisted enforcement. LW's position reflects a view that the burden of proof should fall on institutions to demonstrate non-discrimination before deploying discriminatory tools. CT/RW's position reflects a view that imperfect tools with robust procedures are better than no tools. These are different risk thresholds, not different facts.

### 2.2 Market Mechanisms vs. Regulatory Mandates as the Primary Change Driver

**The disagreement:** RW argues that institutional competition on assessment quality, credential unbundling, and market accountability through published outcome data will drive improvement more effectively than top-down regulation. LW/CT/EC argue that market mechanisms fail to reach the institutions that need change most urgently, and that regulatory mandates — despite their imperfections — create forcing functions that voluntary good practice does not.

**Best argument for RW:** QĐ 1705 was issued without integrity provisions, demonstrating that regulatory actors are not reliably better aligned with student interests than market actors. The BUV AIAS success was driven by skilled educators (Perkins) implementing a model that works, not by regulatory mandate. Market-generated best practice spreads through competitive imitation when it produces observable outcome advantages.

**Best argument for LW/CT:** The institutions with the weakest assessment design and highest fraud rates are not competitive prestige institutions that face market accountability for graduation quality. They are institutions serving students with fewer alternatives, where market pressure is weakest. Voluntary good practice is adopted most readily by institutions that need it least. Only regulatory mandate creates improvement requirements for the full distribution of institutions.

**Why this cannot be resolved by evidence alone:** This is a political economy question about whether Vietnam's MOET can produce and enforce regulation aligned with student welfare, rather than with institutional or commercial interests. The answer depends on political facts that are disputed and contingent. It is also a values question about the relative weight of market failure risks versus regulatory capture risks — a question where different foundational commitments about state capacity and market reliability produce different conclusions.

### 2.3 Immediate Prohibition vs. Procedural Reform for AI Detection in Vietnam

**The disagreement:** LW calls for immediate MOET prohibition of AI detection tools trained on native-English corpora in Vietnamese proceedings until bias auditing is complete. RW/CT call for procedural reform — human review requirements, bias audit requirements, appeals processes — without a blanket prohibition.

**Best argument for LW:** The harm from deploying biased tools while "improving procedures" falls in real time on real students who are wrongly accused. Vietnamese institutions, implementing detection tools in an attempt to demonstrate international standards alignment, will not spontaneously develop the institutional competence to prevent ESL discrimination without a specific prohibition creating a forcing function. Given that better alternatives (oral defense, AIAS) exist and are immediately deployable, there is no educational argument for accepting the discrimination risk of detection tool deployment.

**Best argument for CT/RW:** Blanket prohibition leaves institutions without any mechanism to address genuine fraud during the transition period to assessment redesign, which takes time to implement. A procedural framework — detection as soft signal only, with mandatory human review and bias-audited tools — protects against the documented harms while preserving some fraud deterrence during the transition.

**Why this cannot be resolved by evidence alone:** This is a values question about risk tolerance. How much discrimination risk is acceptable during a transition period? Different answers reflect different weights on Type I error (falsely accusing innocent students) versus Type II error (missing genuine fraud), and different assumptions about how quickly Vietnamese institutions can implement assessment redesign at scale.

---

## 3. The Irreconcilable Differences

These are positions where the foundational values are genuinely incompatible, not merely different in emphasis. Compromise language cannot paper over these differences.

### 3.1 What Education Is For

**LW's position:** Education is primarily a social and human process aimed at genuine intellectual development, democratic participation, and human flourishing. The credential-as-sorting-mechanism is a neoliberal distortion of this purpose. Academic integrity defined primarily as credential authenticity is defending the sorting function, not education itself.

**RW's position:** The credential system is a legitimate, if imperfect, market mechanism for signaling competency and enabling labor market sorting. Improving that system through better competency verification and market accountability is the appropriate goal. The credential itself is not a distortion — its monopoly status is.

**Why irreconcilable:** These are different answers to the foundational question of what a university is for. No amount of evidence about fraud rates, false positives, or assessment efficacy resolves the prior question of whether the institution should be optimizing for credential quality or for human development, when these come into tension. LW's prescription leads toward reduced grade pressure, collaborative knowledge-building, and student agency in curriculum. RW's prescription leads toward stronger competency verification and credential unbundling. The policies are different because the goals are different.

### 3.2 Institutional Actors as Trustworthy vs. Captured

**LW's position:** EdTech companies (Turnitin, GPTZero) are primarily commercial actors whose interests are misaligned with genuine educational outcomes. They maintain the panic about AI fraud because that panic is their market. Universities that outsource academic integrity to these companies are surrendering their moral frameworks to parties whose business model depends on the continuation of the problem.

**RW's position:** Educational bureaucracies are equally subject to institutional self-interest and competence failures. The Texas A&M case was a bureaucratic failure, not a market failure. The Hindawi retraction catastrophe was driven by academic institutional incentives (publish-or-perish), not by EdTech companies. Private-sector solutions (Khanmigo's Socratic design, Coursera's viva model) outperform institutional equivalents on the integrity metrics LW values.

**Why irreconcilable:** This is a prior disagreement about whether market actors or institutional actors are more reliably aligned with public interests. Neither side denies that both types of actors can fail — they differ on which failure mode is more prevalent and more dangerous. This prior shapes every policy prescription that follows.

### 3.3 ESL Students as Individual Rights-Bearers vs. Policy Tradeoff Variables

**LW's position:** The 61.3% false positive rate for ESL writers is a civil rights problem. Deploying tools with this disparity is institutionalized discrimination, not a regrettable policy tradeoff. The harm to wrongly accused students is not an "acceptable cost" of maintaining detection infrastructure — it is a categorical injustice that makes any detection deployment morally impermissible until the bias is eliminated.

**CT/RW's position:** The harm to wrongly accused students is real and must be minimized through procedural safeguards. But the harm from undetected fraud — credential inflation devaluing honest students' degrees, human capital destruction in professional contexts, contamination of the research record — is also real. Policy must balance both types of harm, not treat one as categorically prior to the other.

**Why irreconcilable:** LW applies a deontological constraint: certain discriminatory means are impermissible regardless of consequences. CT/RW apply a consequentialist framework: all harms enter the calculation, and the goal is to minimize total harm including both Type I and Type II errors. These are different moral frameworks, not different empirical beliefs.

---

## 4. The Ultimate Solution Framework

This framework synthesizes the consensus zone into concrete, actionable steps, organized by time horizon.

### Immediate Actions
*(can be done now, no legislation required)*

**For institutions:**

1. **Suspend AI detector output as sole disciplinary evidence — effective immediately.** No grade penalty or misconduct finding based solely on Turnitin AI Detection, GPTZero, or equivalent tools. Every detection flag requires a direct conversation with the student, review of process evidence (draft history, prior drafts submitted), and institutional review before any formal finding. This is what Turnitin's own guidelines recommend and is currently being violated by most institutions using these tools.

2. **Implement spot viva for all high-stakes written assessments.** For any assessment worth more than 20% of course grade: random sampling at 10-15% of submitted work for a 15-20 minute oral follow-up. Examiner questions drawn directly from the submitted work. No specialist technology required — only rubric development and scheduling infrastructure, both of which are low-cost.

3. **Adopt the AIAS (AI Assessment Scale) framework for all course designs.** Every assignment specification should state which AIAS level applies. AIAS Level 1 (no AI) for personal reflection, authentic situated tasks, and examinations. AIAS Level 3-4 (disclosed and bounded AI use) for research and collaborative work. This replaces ambiguity — the primary driver of underground AI use — with clarity.

4. **Publish an explicit AI use policy at course level, every semester.** Students cannot be held accountable to standards they were not clearly informed about. A single-page AI use statement per course syllabus is the minimum viable notice. This is a Bretag "Access" element failure in most current institutions and is fixable with zero cost.

**For Vietnam specifically:**

5. **Prohibit AI detectors trained exclusively on native-English corpora from use as evidence in any proceedings involving Vietnamese-English-medium students** until independent bias auditing for Vietnamese student writing has been conducted. The ESL false positive disparity (61.3% vs. 1.5%) makes these tools potentially more discriminatory in Vietnam's internationalization context than in any other setting documented in the literature. This is a specific MOET directive that can be issued without amending existing regulations.

6. **Mandate an AI use disclosure statement on all academic submissions.** One additional field on submission forms: "AI was not used in preparing this work" or "AI was used as follows: [specification]." False declaration is an explicit integrity violation. This operationalizes Eaton's postplagiarism principle — the ethical line is misrepresentation, not AI use — at no institutional cost.

### Medium-Term Reforms
*(1-3 years, requires institutional policy)*

7. **MOET Ministerial Circular bridging Decree 109/2022 and QĐ 1705/QĐ-TTg.** The policy gap between Vietnam's academic integrity regulations (no AI provisions) and its AI adoption strategy (no integrity safeguards) is the structural vacuum in which 3x-the-acknowledged fraud is occurring. A circular should: (a) define AI-assisted academic misconduct within existing Decree 109 categories; (b) mandate AIAS-compliant AI use policy at institution level; (c) require AI disclosure on all submissions; (d) prohibit detection tool output as sole disciplinary evidence; (e) establish national annual reporting on confirmed AI misconduct cases. This is achievable in one ministerial cycle.

8. **Standardize national penalty schedules for AI misconduct.** Vietnam's HCMUFA case (50% grade deduction) versus NTU Singapore (zero marks) and CUHK (potential expulsion) creates arbitrage incentives for students at lenient institutions. A tiered national schedule — warning for first low-stakes offense, zero assignment for moderate fraud, course failure for severe or repeat fraud — standardizes the cost-of-fraud calculation and reduces penalty arbitrage across institutions.

9. **Fund structured professional development in AI-era assessment design.** A three-year faculty development program: Year 1 — understanding AI capabilities and assessment audit (which current assessments are AI-vulnerable); Year 2 — piloting redesigned assessments with structured peer feedback; Year 3 — departmental scaling and case study publication. QĐ 1705's teacher capacity development mandate is the funding hook. Assessment redesign mandates without educator preparation are policy theater.

10. **Require independent bias audits for any AI detection tool deployed in Vietnamese educational enforcement contexts.** Any tool deployed must demonstrate maximum false positive rate for Vietnamese-language and Vietnamese-English-medium writing, independently audited. This mirrors EU AI Act Article 10 bias requirements and EU AI Act Annex III high-risk classification for educational AI. The standard should be set at no more than a 2:1 disparity between ESL and native-speaker false positive rates — a fraction of the current 40:1 documented disparity.

11. **Invest in oral defense infrastructure, not detection infrastructure.** Vietnamese institutions currently evaluating Turnitin subscriptions should redirect that budget to TA training for viva rubric design, scheduling systems for spot viva logistics, and AIAS template development. The cost is comparable; the five-year durability is not — detection infrastructure will be functionally obsolete against open-source locally-run models by 2028, while oral defense remains robust indefinitely.

### Long-Term Structural Changes
*(3-10 years, requires legislation and/or cultural shift)*

12. **International regulatory coordination for LLM watermarking.** The collective action problem (Aaronson's OpenAI experience: unilateral watermarking creates competitive disadvantage) requires multilateral mandate. Vietnam should advocate through ASEAN AI governance forums for mandatory watermarking standards for commercially deployed LLMs in educational contexts, consistent with EU AI Act Article 50 direction and China's existing AI-generated content labeling requirements. This is a low-cost advocacy position with potentially high long-run returns.

13. **Publisher-side citation verification mandate.** The NeurIPS 2025 hallucinated citation crisis and Hindawi retraction catastrophe are both addressable through mandatory DOI verification at manuscript submission stage. COPE and CrossRef have the technical infrastructure; what is missing is industry-wide coordination to require it. This is the research integrity equivalent of food safety labeling — the technology exists, the collective action barrier requires governance to overcome.

14. **Honor code culture development as a multi-year institutional investment.** McCabe's 25-30% lower cheating rate in honor code institutions is the largest effect size in the academic integrity literature. It requires genuine cultural implementation — not ceremonial pledge, but consistent faculty modeling, student ownership of integrity values, and institutional norms that treat integrity as a community good rather than a compliance obligation. This cannot be mandated; it must be cultivated. The payback period is years, not semesters, but the steady-state efficiency gain — eliminating need for expensive detection and adjudication infrastructure — is substantial.

15. **Credential unbundling and competency verification infrastructure (long-run structural fix).** Employer competency testing, portfolio verification, and work-sample assessment reduce the return on credential fraud by providing alternative signals that are harder to fake. This operates through labor market evolution and is most relevant in professional services and technology sectors where competency is directly observable. Its applicability to Vietnam's public sector and credential-gated professions is limited in the medium term; its importance increases as the formal labor market matures.

### For Vietnam Specifically: What Is Realistic

**What is achievable in 2026:** MOET Circular, AIAS framework adoption, suspension of sole-evidence detection, ESL bias prohibition, spot viva piloting in 5-10 institutions building on the BUV model. None of these require new legislation. All have precedent in comparable education systems (BUV pilot in Hanoi, Australian TEQSA recognition of AIAS, New Zealand and Canadian process-based assessment models).

**What requires realistic caution:** Vietnam's tự chủ đại học (university autonomy) reforms have created institutional performance incentive structures that can generate domestic publish-or-perish pressures. National policy frameworks must explicitly engage with research promotion criteria, not just assessment policies, to prevent the Hindawi-style institutional dynamic from emerging domestically.

**What should be avoided:** Purchasing English-medium detection tool subscriptions as a demonstration of international standards alignment. The combination of ESL bias (40:1 false positive disparity) and absent institutional competence infrastructure is predictable and avoidable. Early-mover Western institutions made expensive mistakes in 2022-2024 so that Vietnam does not have to.

---

## 5. What Cannot Be Accepted

These proposals were rejected by multiple participants across ideological lines. They represent positions that no serious analyst at this table endorses, regardless of political orientation.

**1. AI detector output as primary or sole evidence in academic misconduct proceedings.**
Rejected by RW, LW, CT, EC, ED, and TE — unanimously. The 61.3% ESL false positive rate (Liang et al. 2023), independent of any ideological position on regulation, market mechanisms, or student accountability, disqualifies these tools from serving as standalone disciplinary evidence. Any institutional policy that allows grade penalties or misconduct findings based solely on Turnitin AI or GPTZero output fails basic evidentiary standards.

**2. Blanket AI prohibition policies as the primary integrity response (CUHK model).**
Rejected across the board, though for different reasons. TE: technically infeasible against personal devices and locally-run open-source models. EC: economically counterproductive (prevents legitimate AI skill development, drives fraud underground, increases concealment). LW: disproportionate enforcement falls on students without social capital to navigate appeals. RW: chills legitimate EdTech innovation. ED: doesn't address the underlying assessment design failure. CT: BUV's AIAS pilot shows that tiered, contextual frameworks outperform blanket prohibition.

**3. Continuous keystroke monitoring, biometric proctoring, and surveillance-as-integrity infrastructure.**
Rejected unanimously. LW frames this as a civil rights issue — eye movement tracking, keystroke dynamics, and facial expression monitoring in students' homes violate dignity and are particularly harmful to students with disabilities and those in shared living situations. ED frames it as pedagogically damaging — surveillance architectures transform the educator-student relationship from trust-based to adversarial, producing students skilled at evasion rather than students who have internalized integrity as a personal value. TE frames it as technically futile — sophisticated students bypass behavioral monitoring through external devices while legitimate students bear the full cost.

**4. Treating AI detection as a solved technical problem.**
Rejected by TE (explicitly), EC (arms race analysis), and implicitly by all participants. The academic literature (Liang et al. 2023; Weber-Wulff et al. 2023) is clear that current tools are unreliable, biased, and trivially evaded. Administrators and policymakers who present detection deployment as a comprehensive institutional response are not reading the evidence base. Turnitin's 98% claimed accuracy versus 50% independent testing accuracy is not noise — it reflects fundamentally different evaluation conditions.

**5. Relying exclusively on voluntary student AI disclosure without structural verification.**
Rejected by EC (the 3x concealment rate in Vietnam provides direct evidence that honor-system-alone approaches do not produce honest disclosure under current incentive structures), and endorsed only as one element in a multi-layered system. Self-disclosure requirements create a legal and moral obligation that slightly raises the psychological cost of fraud, but as a primary enforcement mechanism they are inadequate under the documented incentive structure.

**6. Delegating academic integrity frameworks entirely to international EdTech vendors.**
Rejected by LW (Selwyn's corporate ethics critique, accepted in its core by CT and ED), CT (BUV's locally-adapted AIAS pilot outperforms imported US/Australian frameworks directly), and ED (faculty must retain professional authority to define what learning is and how it should be assessed). Academic institutions that outsource their moral frameworks to companies whose business model depends on the continuation of the problem — Turnitin's detection revenue is maintained by the fraud panic — are not practicing institutional governance.

**7. Applying any enforcement action against students without prior AI literacy education and clear policy communication.**
Rejected by all participants as a basic procedural justice requirement. Students who have not been taught what is prohibited cannot be held to standards that were not communicated. The Texas A&M, UK OIA, and HCMUFA cases all share a common feature: enforcement preceded clear policy communication. This is not a technicality — it is a foundational due process requirement.

---

## 6. Open Questions

These are questions where the current evidence is insufficient for confident policy conclusions. More research is needed before these can be resolved.

**1. What are the actual false positive rates for AI detection tools applied to Vietnamese-medium and Vietnamese-English-medium student writing?**
Liang et al. tested TOEFL essays by Chinese college students. The Vietnamese ESL context — with specific features of Vietnamese-influenced English writing, Vietnamese-medium submissions, and Vietnamese academic writing conventions — has not been directly studied. The implication that Vietnamese students face the documented ESL false positive risk is credible but not directly measured. A validation study of major detection tools against Vietnamese student corpora would be immediately policy-relevant and is currently absent from the literature.

**2. How does tự chủ đại học (university autonomy) affect academic integrity incentives in Vietnamese institutions?**
RW flagged this concern: university autonomy expansion introduces institutional performance management frameworks (publication targets, international ranking incentives, enrollment growth pressures) that can generate domestic publish-or-perish pressures analogous to the Hindawi retraction dynamic at an international level. The extent to which Vietnamese institutional autonomy is already generating these incentive distortions is not yet documented in the academic integrity literature.

**3. Does the AIAS framework produce sustained integrity improvements beyond the short term?**
BUV's pilot demonstrated measurable reduction in AI-related misconduct during the intervention period. What is unknown is whether these improvements persist after the novelty effect of policy change dissipates, whether they scale to institutions without Perkins-level implementation leadership, and whether they produce equivalent results across different Vietnamese institutional contexts (public research universities vs. regional colleges vs. private institutions). Longitudinal evidence is needed.

**4. What is the optimal penalty severity in Vietnam's specific cost-benefit context?**
EC's analysis establishes that deterrence requires raising the expected cost of fraud to exceed the expected benefit. The benefit of fraud in Vietnam's credential-premium context is high; the current penalty schedule (HCMUFA: 50% deduction, the softest in the regional peer set) is likely insufficient for deterrence. But the optimal penalty level — high enough to deter but calibrated to the severity of the offense and the due process protections required — has not been empirically studied in Vietnam's specific institutional and labor market context.

**5. When will watermarking become a regulatory reality in commercially deployed LLMs?**
TE's framework positions watermarking as the correct long-term technical solution pending regulatory coordination. The EU AI Act Article 50 requirements are entering effect progressively through 2025-2026. Google DeepMind's SynthID text watermarking is in limited deployment as of 2025-2026 but has not been extended to production scale. The timeline for commercial LLM watermarking becoming standard — and therefore usable for educational attribution — is technically and regulatorily uncertain. Policy frameworks built around watermarking as a near-term tool are currently premature; its emergence as a medium-term tool is possible and worth monitoring.

**6. Can institutional honor code cultures be deliberately built, and over what time horizon?**
McCabe's empirical finding establishes the outcome — honor code cultures produce 25-30% lower cheating rates. The mechanism is cultural, not procedural. What is insufficiently studied is the specific institutional practices that build genuine honor code culture (as opposed to ceremonial pledge programs that produce no measurable effect), the time horizon over which culture change produces measurable integrity improvements, and whether these mechanisms work equivalently in Vietnamese Confucian-influenced educational culture as in the Anglo-American contexts McCabe primarily studied.

**7. What is the interaction between AI fraud and brain drain in Vietnam's specific context?**
EC proposed that credential inflation from AI fraud could accelerate brain drain by contaminating the signal value of Vietnamese degrees in international labor markets — the most mobile and highest-ability graduates are most affected by this signal degradation. This mechanism is theoretically well-founded (Akerlof's lemons model applies directly) but empirically unstudied in the Vietnamese context. If true, it is one of the most consequential long-run effects of unchecked AI fraud in Vietnam, and would significantly alter the cost-benefit calculation for policy urgency.

---

## Conclusion

The six-participant debate produced an unusual degree of convergence on both diagnosis and primary intervention. The root cause analysis — structural incentives, not moral failure — is accepted across the ideological spectrum. The primary intervention — oral defense and process-based assessment — is endorsed by a free-market analyst, a critical EdTech activist, an institutional pragmatist, an education economist, a learning scientist, and a machine learning researcher. The red line against sole-evidence AI detection was unanimously held.

What the debate clarified is that the disagreements remaining after this consensus are mostly about sequencing, mechanism, and risk tolerance — not about the direction of change. Vietnam's specific context sharpens the urgency: the combination of high credential premium, ESL majority students, detection tools trained on native-English corpora, tự chủ đại học performance pressures, and a policy gap between Decree 109 and QĐ 1705 creates a distinctive and serious vulnerability.

The institutions that will successfully navigate this challenge are not those that deploy the most sophisticated detection algorithms. They are those that design assessments that require authentic intellectual engagement, build cultures that make integrity personally meaningful rather than bureaucratically imposed, and resist the commercially convenient solution of outsourcing moral frameworks to companies whose profits depend on the continuation of the problem.

That is not ideology. It is the evidence.

---

*Report prepared for Nhập môn Khoa học Giáo dục (25CGD), Buổi 5, HCMUS, Semester 2 2025-2026.*
*Source materials: six position papers (right_wing, left_wing, center, economist, educator, technologist).*
*Key empirical grounding: Liang et al. 2023; McCabe et al. 2012; Gallant 2008; Eaton 2021/2023/2024; Perkins et al. 2023 (AIAS); Kirchenbauer et al. 2023; Nguyen et al. 2024 (Springer Vietnamese study); Retraction Watch 2023-2025.*
