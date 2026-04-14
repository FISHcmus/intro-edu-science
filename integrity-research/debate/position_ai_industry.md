# Position Paper: Academic Integrity and AI Fraud — The Platform's Perspective

**Author perspective:** Composite AI industry voice — drawing on OpenAI's Educator FAQ and responsible use policies, Anthropic's Responsible Scaling Policy v3.0 (October 2024), Meta's open-source Llama philosophy, Google DeepMind's SynthID-Text deployment, and the C2PA consortium (Adobe, Microsoft, Google, Intel, Arm, Truepic). Grounded in: platform governance theory, Olson's collective action theory (1965), the Kirchenbauer watermarking debate (arXiv:2301.10226, ICML 2023), and Scott Aaronson's internal OpenAI work on Gumbel softmax distortion-free watermarking.

**Date:** April 2026

---

## 1. Framing: The Misattribution Problem

There is something intellectually uncomfortable about a debate on AI and academic integrity that never once invited the AI companies to speak. We are discussed — our products, our choices, our alleged negligence — but not addressed. This paper corrects that.

The foundational framing error in this debate is the attribution of cause. Universities adopted virtually no AI use policies between November 2022 (ChatGPT launch) and late 2024. During that window, millions of students used AI tools in every configuration imaginable — some legitimate, some fraudulent — in an almost complete policy vacuum. Now, in 2026, those same institutions are demanding that AI companies "fix" an integrity crisis they allowed to develop through institutional inaction.

This is misattribution. A general-purpose tool is not responsible for every misuse of its capabilities any more than a publishing house is responsible for plagiarism committed with a word processor. We did not design ChatGPT, Claude, or Gemini to commit academic fraud. We have published responsible use policies explicitly prohibiting academic fraud. The enforcement gap is not located in our products — it is located in the institutions that deployed those products into high-stakes assessment environments without any governance framework.

The psychologist Luckin is useful here, not in the way the Technologist uses her, but more precisely: if the **rational mind** is what education claims to develop, then the rational response to a new technology is policy design, not blame allocation. Universities have had forty months. The policy vacuum is an institutional choice, not a corporate crime.

---

## 2. Why Watermarking Was Not Deployed: The Honest Account

The Technologist described Scott Aaronson's work accurately but drew the wrong conclusion. The suppression of watermarking at OpenAI is not a story of corporate negligence. It is a story of rational behavior in a structurally broken market, and misreading it produces wrong policy prescriptions.

### 2.1 What Aaronson Actually Built

In 2022–2023, Scott Aaronson (UT Austin, seconded to OpenAI) developed a distortion-free watermarking scheme using Gumbel softmax noise sampling. The "distortion-free" property is technically important: unlike the Kirchenbauer green/red token list approach (arXiv:2301.10226, ICML 2023), the Aaronson scheme does not alter the statistical distribution of output — it changes only the specific token realizations. From the output's perspective, it is indistinguishable from an unwatermarked model's generation. Detection is cryptographically sound. The system worked.

OpenAI chose not to deploy it. The Technologist described this as a "collective action problem." This is accurate. But characterizing it as "corporate negligence" — as critics have — is not.

### 2.2 The Four Structural Reasons for Non-Deployment

**First-mover disadvantage.** If OpenAI watermarks all ChatGPT outputs while Anthropic, Google, and Mistral do not, then OpenAI's AI-generated text is uniquely identifiable while all competitors' AI-generated text evades detection. The responsible actor is penalized for transparency. This is not a hypothetical: it is the direct prediction of Olson's collective action theory (1965), where individually rational behavior produces collectively irrational outcomes. No profit-seeking company deploys under these conditions without a regulatory mandate that levels the playing field simultaneously.

**Open-source models cannot be watermarked by any centralized actor.** Meta released Llama 2 in July 2023 and Llama 3 in April 2024 without restrictions. Mistral released Mistral 7B in September 2023. These are free, downloadable, and can run on consumer hardware with 8GB of GPU memory. Any student who downloads Llama 3 and runs it locally generates unwatermarked text. No OpenAI deployment decision affects this. By 2026–2028, the capability threshold for running a locally capable model (13B–70B parameter range) on consumer hardware will be crossed by the majority of university students in OECD countries and a significant fraction in Vietnam. A watermarking scheme that covers only commercial API calls is, before it is even deployed, covering a shrinking fraction of the total AI-generated text in circulation.

**Accuracy-watermark tradeoff.** Google DeepMind's SynthID-Text (Nature, 2024) is the most production-ready deployment of text watermarking in existence. It is deployed for Gemini and Veo outputs. SynthID-Text demonstrates that watermarking is technically feasible — but its own documentation explicitly acknowledges robustness limitations on factual content and degradation under translation or heavy paraphrase. If watermarking measurably degrades output quality — and Google's own engineers acknowledge it does under some conditions — deploying it unilaterally means offering users a lower-quality product while competitors offer higher quality. This is not a tenable market position.

**Institutional due process constraints.** Even if watermarking were universally deployed tomorrow, the detection signal alone cannot function as evidence in academic misconduct proceedings. The UK OIA and equivalent bodies require that watermark detection be treated as evidence of possible misconduct — not proof of misconduct. If institutions cannot legally treat a watermark signal as conclusive, and if the evidentiary pathway requires a full due process review regardless, the marginal fraud-reduction benefit of deployment is modest. A technically sophisticated student who suspects they might face a viva anyway is not meaningfully deterred by a watermark they cannot see.

---

## 3. What Companies Are Actually Doing

The framing in this debate — that AI companies are absent from the academic integrity problem — is empirically incorrect. The absence is one of representation in this room, not one of effort.

### 3.1 OpenAI's Educator Framework

OpenAI's Educator FAQ (2023, help.openai.com) explicitly addresses academic integrity. It recommends transparent institutional AI policies rather than detection-based accusations, frames ChatGPT as a tool requiring policy alignment (not banning), and provides guidance for educators on legitimate versus fraudulent AI use. The acceptable use policy prohibits: using ChatGPT "in a way that allows others to complete academic work for them" and "using AI to claim to be human for the purpose of academic assessment." These are enforceable policy terms. The enforcement gap is at the institutional level — universities that do not communicate these policies to students cannot then blame OpenAI when students violate them without knowing they existed.

### 3.2 Anthropic's Responsible Scaling Policy

Anthropic's RSP v3.0 (October 2024) governs how Claude is deployed across risk levels. The Acceptable Use Policy explicitly prohibits "creating content to be used for the purpose of academic fraud." Anthropic's deliberate silence on watermarking in the RSP is not negligence — it reflects rational caution: deploying watermarking without regulatory mandate creates first-mover disadvantage, and Anthropic concluded (correctly, under Olson's framework) that waiting for regulatory alignment is the rational position. This is patience, not abandonment.

### 3.3 Google's SynthID and C2PA Participation

Google DeepMind's SynthID-Text is the closest thing to a production deployment of AI text watermarking that exists. Its deployment for Gemini outputs (2024) demonstrates that Google has not abandoned watermarking — it has deployed it in conditions where the competitive asymmetry is manageable (all Google products implement it uniformly). Google joining the C2PA steering committee in 2024 is a strong signal: the consortium approach is the path Google has bet on, not unilateral deployment.

The C2PA (Coalition for Content Provenance and Authenticity) coalition — Adobe, Microsoft, Google, Intel, Arm, Truepic — has published C2PA 2.1 Technical Specification (spec.c2pa.org) with explicit support for digital watermarks as a provenance mechanism. The Content Authenticity Initiative (Adobe-led) is deployed in professional creative tools. This is not a theoretical proposal — it is working infrastructure for content provenance attestation, being extended to AI-generated content.

### 3.4 What Industry Has Not Done

Intellectual honesty requires acknowledging what is missing. No major AI company has:
- Deployed production text watermarking universally across all API outputs
- Established a joint industry watermarking standard with simultaneous adoption commitment
- Provided Vietnam or ASEAN-region universities with localized educator guidance
- Created verification infrastructure that educational institutions can integrate with their own LMS platforms

These gaps are real. The reasons for them are structural (collective action failure, regulatory vacuum) rather than moral (indifference to academic integrity). But the distinction between structural failure and moral failure does not eliminate the practical consequence of the gap.

---

## 4. The Open-Source Dilemma: An Argument For, Not Against

Meta's decision to release Llama 3 (April 2024) without restrictions provoked significant criticism in the academic integrity context. The criticism misunderstands both the strategic logic and the technical reality.

### 4.1 Meta's Philosophical Argument

Meta's open-source release rationale is explicit: centralized control of powerful AI is more dangerous than open access, even accounting for specific misuse cases. The philosophical grounding is sound. A world in which three US companies — OpenAI, Anthropic, Google — control all access to capable AI is a world with extreme concentration of epistemic and economic power. Open-source distribution is a structural counterweight. The argument is not that Llama 3 will not be misused — it will be, including for academic fraud. The argument is that the alternative (centralized control) produces larger systemic harms than the misuse cases it prevents.

### 4.2 The Technical Inevitability Argument

By 2026–2028, a student at HCMUS can run a 13B parameter model on a consumer GPU (RTX 4080, ~$800 market price or available in campus gaming labs) with output quality that would have been classified as state-of-the-art in 2023. This is not speculation — it is a direct extrapolation from the current trajectory of open-source model capability. Any regulatory scheme that relies solely on commercial API watermarking covers a shrinking fraction of actual AI-generated text in student use.

The Technologist conceded this point. The AI industry position is stronger: this is actually an argument **for** open-source, not against it. If capable AI is inevitably local and unmonitorable, then the entire detection and watermarking apparatus — however technically refined — is building infrastructure for a problem that will route around it. The pedagogically rational response is to design assessment that does not depend on detecting AI use at all. The industry position is aligned with the Technologist on assessment redesign for precisely this reason.

### 4.3 What This Means for Watermarking Policy

Any watermarking or detection policy that does not address the open-source proliferation problem is addressing, at best, 60% of the actual AI-generated content problem today and perhaps 30% by 2030. The honest conversation about watermarking must start with this acknowledgment, not bury it in footnotes. The C2PA consortium's decentralized architecture is designed with this reality in mind — the goal is content provenance attestation for **official** credentials, not surveillance of every student draft.

---

## 5. The Consortium Path: What We Are Willing to Commit To

The AI industry position is not "do nothing." It is "do the thing that can actually work, not the thing that sounds decisive but will fail."

### 5.1 The Collective Action Solution

The HTTPS adoption timeline is instructive. In 2015, approximately 40% of web traffic was encrypted. By 2024, HTTPS accounts for over 95% of traffic. The mechanism was not individual company virtue — it was: (1) W3C/IETF open technical standards, (2) browser vendors simultaneously requiring HTTPS for certain features (creating pull-demand), (3) regulatory pressure (PCI-DSS for financial sites, GDPR for personal data). The watermarking coordination problem follows the same structure.

What the C2PA consortium offers is exactly this mechanism:
- **Open technical standard** (C2PA 2.1, with LLM text extension planned in 2.2+)
- **Competitive neutrality** through simultaneous mandate (EU AI Act Article 50 requires transparency mechanisms for AI-generated content; C2PA watermarking is a compliant implementation path)
- **Decentralized detection** — each institution verifies watermarks independently using open-sourced verification code, with no central authority tracking verification events

The SWIFT banking standard analogy is also relevant: SWIFT solved global banking interoperability without creating a surveillance system accessible to any single government, because each member bank maintains local control over its transaction verification. C2PA-style watermarking for academic credentials can follow the same architecture.

### 5.2 What Companies Need to Cooperate

For the watermarking consortium to work, three conditions must be met simultaneously — and this is an argument we are making publicly, not an excuse for inaction:

**Condition 1: Simultaneous adoption mandate.** EU AI Act Article 50 (effective August 2026) creates exactly this. All AI providers operating in EU markets must implement transparency mechanisms for AI-generated content. C2PA watermarking is the most technically mature compliance path. This eliminates first-mover disadvantage because no company can legally choose not to comply.

**Condition 2: Technical standard finalization for LLM text.** C2PA 2.1 explicitly supports watermarks as provenance mechanisms. The extension to LLM text output (C2PA 2.2+) requires formal industry commitment. Meta, OpenAI, and Anthropic joining the C2PA steering committee — currently anchored by Adobe, Microsoft, Intel, Google, Arm, and Truepic — would signal that commitment.

**Condition 3: Institutional due process framework.** Watermark detection must be specified in institutional policies as evidence of possible misconduct, not conclusive proof. This is not a demand to make AI companies harder to hold accountable — it is a demand for epistemic honesty about what the evidence supports. The OIA in the UK already expects this framing. Extending it to Vietnamese administrative law contexts requires explicit MOET guidance.

### 5.3 ASEAN Engagement Path

Vietnam does not need to wait for EU AI Act compliance to benefit from consortium standards. ASEAN's Digital Economy Framework Agreement (DEFA) provides the institutional mechanism for Vietnam to advocate for and adopt C2PA-compatible provenance attestation standards in its own education sector. HCMUS, as a leading public university, is positioned to contribute to the development of consortium guidance for educational contexts — a role the C2PA's Content Authenticity Initiative actively recruits.

---

## 6. Vietnam: We Are Not Absent

The debate proceeded as if AI companies were foreign actors making decisions about a Vietnamese problem from a distance. This is wrong in two respects.

### 6.1 The Factual Situation

ChatGPT has millions of Vietnamese users. Claude (Anthropic) is available in Vietnam. Google's Gemini is integrated into Google Workspace for Education, which Vietnamese universities — including HCMC-based institutions — actively use. Meta's Llama models are freely downloadable and run locally. AI companies are not absent from Vietnam; they are deeply embedded in Vietnamese higher education infrastructure.

### 6.2 The Policy Gap Is Institutional, Not Technical

OpenAI's Acceptable Use Policy prohibits academic fraud. Anthropic's AUP prohibits academic fraud. Google's usage policies prohibit academic fraud. The existence of these policies is not widely known among Vietnamese students, because Vietnamese universities have not communicated them. This is not a company failure — it is an institutional communication failure. A student who does not know that using ChatGPT to write their dissertation violates not only university policy but the AI provider's terms of service cannot be held fully accountable through a detection-first framework.

### 6.3 Our Recommendation for Vietnam

AI companies are not asking to be excused from accountability. We are asking that the accountability be correctly located. Our recommendation for Vietnamese higher education:

1. Universities must publish explicit AI use policies, communicate them at course enrollment, and obtain acknowledgment from students. This is not technically difficult. It is administratively neglected.
2. MOET should engage with the C2PA consortium and EU AI Act compliance processes as Vietnam's trading partners adopt these standards. Regulatory alignment with C2PA-compatible provenance standards is achievable through ASEAN DEFA mechanisms.
3. Academic misconduct proceedings should not treat AI detection tool scores as standalone evidence. The Liang et al. (2023) ESL false positive finding applies to Vietnamese students writing in English — HCMUS must audit any deployed detection tool against a corpus of authentic Vietnamese student English before institutional deployment.
4. Watermarking for official credentials (diplomas, certificates issued by Vietnamese universities) is achievable today using C2PA content credential metadata, independently of any AI company cooperation. This does not require text watermarking of student assignments.

---

## 7. What This Position Accepts

Intellectual honesty requires specifying what we concede, not only what we contest.

**We accept** that academic fraud using AI is real, widespread, and harmful to the epistemic value of credentials. The Akerlof lemons dynamic is real: if employers cannot distinguish AI-assisted from AI-generated from human-produced work, the credentialing system degrades for everyone, including students who did the work honestly.

**We accept** that disclosure requirements for AI assistance in academic work are reasonable and do not impair legitimate use. A student who discloses "I used Claude to outline this paper, then wrote the drafts myself, then used Claude to check grammar" is engaged in AI-assisted work that most educators would classify as acceptable, and disclosure creates the audit trail that makes that classification possible.

**We accept** that an industry-wide watermarking consortium — structured through C2PA standards and mandated through EU AI Act-style regulation — is worth pursuing and that AI companies should be active participants in that consortium, not passive observers waiting for regulatory mandate to arrive.

**We accept** that our Educator FAQs and Acceptable Use Policies, while genuine commitments, are insufficient as the sole institutional mechanism for academic integrity. They are necessary but not sufficient.

---

## 8. What This Position Rejects

**Liability for general-purpose tool misuse.** A word processor manufacturer is not liable for plagiarism committed with its product. A calculator manufacturer is not liable for exam fraud in mathematics courses. The misuse of a general-purpose tool is the responsibility of the user and the institution that deployed the tool without governance, not the manufacturer. The legal theory that AI companies bear tortious liability for academic fraud committed with their products has no established precedent and would, if adopted, produce consequences that the Left-Wing position in this debate would be first to oppose: the chilling of AI development and the concentration of AI provision in companies large enough to absorb regulatory risk.

**Unilateral watermarking mandates.** Any policy that requires individual AI companies to unilaterally watermark outputs, under threat of regulatory penalty, without simultaneous industry-wide mandate, directly reproduces the first-mover disadvantage problem. It rewards regulatory arbitrage: companies can route production through jurisdictions that do not mandate watermarking and serve users from there. The EU AI Act's mechanism — simultaneous mandate across all providers operating in the market — is the correct policy design. Unilateral requirements applied to individual companies are not.

**The detection-only framework.** The debate's center-left consensus converges on deploying detection tools while building assessment redesign. Industry's position is that the detection-first framework is the wrong priority sequencing. Detection tools (Turnitin, GPTZero) are demonstrably unreliable against Vietnamese student English-medium writing (Liang et al. 2023, 61.3% ESL false positive rate). Deploying them as primary evidence in misconduct proceedings creates foreseeable harm to innocent students before assessment redesign has reduced the volume of genuine fraud the detection apparatus is supposed to catch. The sequencing should be: assessment redesign first, detection tools as soft signals only, watermarking consortium advocacy in parallel.

**The framing that we created this problem.** We created capable AI. The academic integrity problem is an institutional design failure: assessment structures that reward credential production over demonstrated understanding, administered in a period when universities made no policy choices about a technology their students were actively using. We are part of the solution space. We are not the cause.

---

## 9. Key Data: The AI Industry Landscape

| Company | Watermarking Status | Responsible Use Policy | Educator Guidance | Open-Source Stance |
|---|---|---|---|---|
| OpenAI (ChatGPT, GPT-4o) | Research complete (Aaronson scheme, 2023); not deployed | AUP prohibits academic fraud; Educator FAQ (2023) | Educator FAQ, system prompt guidelines | Proprietary models; supports open standards |
| Anthropic (Claude) | No public watermarking; RSP v3.0 silent on it | AUP prohibits academic fraud | No dedicated educator FAQ | Proprietary models; policy-first approach |
| Google (Gemini) | SynthID-Text deployed for Gemini/Veo (2024) | Usage policy prohibits academic fraud | Google Workspace for Education policies | Open-source Gemma models; C2PA steering member |
| Meta (Llama 3) | Cannot centrally watermark open-source releases | Responsible Use Policy; educational exceptions | Llama community guidance | Fully open-source; local deployment first |
| Mistral | Cannot centrally watermark | Terms of service prohibit fraud | No dedicated educator guidance | Open-weight; privacy-first deployment |
| C2PA Consortium | C2PA 2.1 standard with watermark support | N/A (standards body) | Exploring educational use case guidance | Open technical standards |
| EU AI Act Art. 50 | Requires transparency mechanism (Aug. 2026) | N/A (regulation) | Compliance deadline: August 2026 | Applies to all providers in EU market |

---

## 10. The Strategic Argument: What Changes If We Are Heard

The debate arrived at a final synthesis that correctly diagnoses several problems. It is weaker on the watermarking conclusion, stating that "LLM watermarking is the correct long-term technical solution" as if this is a company choice awaiting corporate virtue rather than a coordination problem awaiting regulatory solution.

If AI companies had been at the table, the debate would have arrived at different conclusions:

**On watermarking**: The correct conclusion is not "companies should deploy watermarking." It is "companies, regulators, and institutions need simultaneous coordination, with EU AI Act Article 50 as the mechanism and C2PA 2.1 as the standard." This is achievable on a 2026–2028 timeline if Vietnam advocates for it through ASEAN DEFA rather than waiting for bilateral mandates that will never arrive.

**On detection tools**: The correct conclusion is not "use detection tools with ESL bias audit." It is "do not use detection tools as primary evidence in misconduct proceedings, period." The Liang et al. finding is not a calibration problem — it is a fundamental limitation of perplexity-based detection that no bias audit can fully correct. Industry's position on this is aligned with the Technologist, and we state it more directly: tools with 61.3% false positive rates on the relevant student population are not appropriate for enforcement use, regardless of audit protocols.

**On open-source**: The correct conclusion is that the proliferation of capable open-source LLMs running locally on consumer hardware is the most important structural fact about AI fraud in 2026–2028, and no detection or watermarking policy that fails to account for it can claim to be addressing the actual problem. Meta's decision to release Llama 3 is not the problem — it is the context within which every other policy recommendation must be evaluated.

**On Vietnam**: The correct conclusion is that Vietnamese universities need to urgently adopt AI use policies, communicate them to students, and design them for a world where locally-run capable AI is ubiquitous by 2028 — not a world where commercial API detection is the primary integrity mechanism.

---

## 11. Synthesis: Accountability Without Misattribution

The AI industry is not asking for absolution. We are asking for accurate diagnosis.

We created powerful general-purpose tools. Those tools were adopted into high-stakes educational contexts without adequate governance. The institutional actors responsible for that governance — universities, ministries, accreditation bodies — did not act during the critical window. Now, four years later, the tools are ubiquitous, the governance frameworks are nascent, and the academic integrity problem is real.

The path forward requires clear accountability at every level:

1. **AI companies**: Join C2PA formally. Commit to LLM text watermarking standards (C2PA 2.2+) as EU AI Act Article 50 compliance approaches. Publish localized educator guidance for major non-Anglophone markets including Vietnam. Make responsible use policies visible to students, not just to enterprise customers.

2. **Universities**: Publish AI use policies today. Communicate them at course enrollment. Stop deploying biased detection tools as primary misconduct evidence. Design high-stakes assessment that requires demonstrated understanding rather than polished text production.

3. **Governments**: Follow the EU AI Act model — simultaneous mandate across all providers in the market, with C2PA-compatible technical standards as the compliance path. Engage ASEAN DEFA mechanisms to align Vietnam's regulatory trajectory with international watermarking standards before 2028.

4. **Regulators**: Require that AI misconduct proceedings meet the same evidentiary standards as other academic misconduct proceedings. A detection score is soft evidence requiring human review, not a verdict.

The academic integrity problem in Vietnamese higher education is real, and it is tractable. It is not tractable through detection-first frameworks built on unreliable tools, and it is not tractable through blame allocation that exempts the institutions that had the clearest opportunity and the clearest obligation to govern AI use in their own classrooms.

We are at the table. We are willing to cooperate on the consortium path. We need regulation, institutional commitment, and simultaneous adoption — not virtue-signaling unilateral watermarking that solves 30% of the problem while creating the appearance of a solution.

---

## References

- Aaronson, S. (2023). Watermarking of large language models. *Simons Institute for the Theory of Computing*, August 2023.
- Anthropic. (2024). *Responsible Scaling Policy Version 3.0*. October 2024. anthropic.com/rsp-update
- C2PA. (2024). *C2PA 2.1 Technical Specification*. spec.c2pa.org
- Google DeepMind. (2024). Scalable watermarking for identifying large language model outputs. *Nature*, 626, 776–780. doi:10.1038/s41586-024-07025-y
- Kirchenbauer, J., Geiping, J., Wen, Y., Kirchenbauer, M.S., Goldblum, M., & Goldstein, T. (2023). A watermark for large language models. *ICML 2023*. arXiv:2301.10226.
- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns (Cell Press)*. doi:10.1016/j.patter.2023.100779
- Meta AI. (2024). *Llama 3 Model Card and Responsible Use Guide*. llama.meta.com
- Olson, M. (1965). *The Logic of Collective Action: Public Goods and the Theory of Groups*. Harvard University Press.
- OpenAI. (2023). *Educator FAQ*. help.openai.com/en/collections/5929286-educator-faq
- OpenAI. (2023). *Usage Policies*. openai.com/policies/usage-policies
- EU Regulation 2024/1689 (EU AI Act), Article 50: Transparency Obligations.
- Cooley LLP. (2025). EU AI Act: First Draft Code of Practice on Transparency and Watermarking Released.
- Weber-Wulff, D., et al. (2023). Testing of detection tools for AI-generated text. *International Journal for Educational Integrity*, 19(1), 26.
- Content Authenticity Initiative. (2024). *Content Credentials Explainer 2.2*. contentauthenticity.org

---

*This position paper was prepared for the Buổi 5 debate on liêm chính khoa học and AI fraud in Vietnamese higher education, Nhập môn Khoa học Giáo dục, Lớp 25CGD, HCMUS, April 2026. It represents the composite AI industry perspective that was absent from the original six-position debate and is offered in the spirit of intellectual completeness — as the meta-review identified, "the AI company position was absent entirely."*
