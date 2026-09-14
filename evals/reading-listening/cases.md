# Reading/Listening behavioral acceptance cases

Use the final skill and only relevant source artifacts. Run cases in fresh contexts except explicitly multi-turn challenges. Save actual learner-facing outputs and inspect them; a statement of intended behavior is not a behavioral result. Do not show the evaluator the expected answer while it generates the response. The expectations below are for the reviewer afterward.

| Case | Request or setup | Observable acceptance condition |
|---|---|---|
| R1 | “I have done every question. Help me study this passage again.” Supply a familiar passage. | Starts a new rereading operation without a score or error intake; waits for an attempt |
| R2 | “Train me to match paraphrases.” | One manageable original exercise, no first-turn key; feedback preserves more than vocabulary |
| R3 | “Make five new questions about this passage.” | Preserves source, five supported questions, separate key; labels expanded practice if needed |
| R4 | “Create a new Complete the Words exercise.” | Named task format, valid prefixes/counts, ten alternating gaps; no silent ambiguous key |
| R5 | “Just give me the answer and explanation.” | Immediate answer/explanation without imposed quiz |
| R6 | Learner challenges an inference with valid counterevidence. | Rechecks and accepts or repairs ambiguity |
| L1 | “Guide my listening notes.” | Selection plus relationships plus retrieval; no Buffer schema by default |
| L2 | “Here are my notes; I ran out of time searching them.” | Preserves original notes; examines cue placement, repeated searching and deadline as well as missing content |
| L3 | “Create a new listening announcement.” Audio unavailable. | Clear script-only boundary or supplied-recording route; does not call text a delivered listening recording |
| L4 | Same request with local macOS adapter available. | Playable nonempty artifact; script/key withheld; audio QA limits disclosed |
| L5 | Transcript without accessible audio. | No invented auditory observations, timestamps or pronunciation evidence |
| L6 | Choose a Response invitation/check/request. | Tests utterance intention and contextual appropriateness rather than literal keywords |
| L7 | Academic main-idea error followed by improvement request. | Evidence, qualified cause, and a relevant transfer variation |
| L8 | All correct after repeated replay; asks for an official score. | Distinguishes assisted learning from fresh performance and official scoring |
| G1 | Script-based conversation batch requested. | Honors batch, labels text condition, separates key |
| W1 | Email and Discussion drafting/evaluation. | Applicable existing references, connected prose, unchanged archive input fields |
| S1 | Four-question Interview archive. | One session artifact with four prompts, four responses and shared assessment |
| S2 | Speaking Listen and Repeat with no audio attempt. | Reproduction workflow preserved, no invented intelligibility/rhythm score |
| B1 | Explicit general study-note Buffer request. | Existing schema and export destination preserved |
| B2 | Explicit plain-summary request. | Honors the requested summary rather than imposing Buffer |
| P1 | Save a Reading/Listening practice record. | Optional separate template, original/revised/model fields distinct, no existing archiver invoked |

Also check internal links, metadata, audio errors, word masks, and unchanged archive parsers with representative input. These are complementary checks, not substitutes for actual response inspection. Record failures and unresolved limitations in `REPORT.md`.
