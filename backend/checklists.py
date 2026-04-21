"""Curated document checklists by visa / status path (MVP guidance only — not legal advice)."""

from enum import Enum

from pydantic import BaseModel, Field


class VisaType(str, Enum):
    """Stable codes the frontend can send; expand as the product grows."""

    F1_OPT = "f1_opt"
    F1_STEM_OPT = "f1_stem_opt"
    J1 = "j1"
    H1B = "h1b"
    DACA_INITIAL = "daca_initial"
    DACA_RENEWAL = "daca_renewal"
    FAMILY_ADJUSTMENT_I485 = "family_adjustment_i485"
    ASYLUM_PENDING_EAD = "asylum_pending_ead"
    NATURALIZATION_N400 = "naturalization_n400"
    OTHER = "other"


class ChecklistItem(BaseModel):
    title: str = Field(..., description="Document or step label.")
    detail: str | None = Field(
        default=None,
        description="Short plain-language note (e.g. what USCIS typically expects).",
    )
    related_form: str | None = Field(
        default=None,
        description="Common USCIS form this item ties to, if any.",
    )


class ChecklistBundle(BaseModel):
    visa_type: VisaType
    display_name: str
    summary: str
    items: list[ChecklistItem]


DISCLAIMER = (
    "This checklist is educational and may be incomplete for your case. "
    "It is not legal advice. Confirm requirements on official USCIS instructions "
    "or with a qualified immigration attorney or accredited representative."
)


def get_checklist(visa_type: VisaType) -> ChecklistBundle:
    bundles: dict[VisaType, ChecklistBundle] = {
        VisaType.F1_OPT: ChecklistBundle(
            visa_type=VisaType.F1_OPT,
            display_name="F-1 Optional Practical Training (OPT)",
            summary="Typical items when filing Form I-765 for post-completion OPT.",
            items=[
                ChecklistItem(
                    title="Form I-765",
                    detail="Completed and signed; correct edition per USCIS.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Government filing fee(s)",
                    detail="Pay per current USCIS fee schedule (check I-765 instructions).",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Passport-style photo",
                    detail="Meet USCIS photo specifications.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Copy of Form I-20",
                    detail="OPT recommendation on page 2; signed by you and DSO within required timeframe.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Copy of passport identity page and current F-1 visa (if any)",
                    detail="Include most recent admission evidence if helpful.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Copy of prior EAD (if any)",
                    detail="Front and back if you were previously granted OPT or other EAD.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="I-94 arrival record",
                    detail="Electronic printout showing F-1 status and admit-until date.",
                    related_form="I-765",
                ),
            ],
        ),
        VisaType.F1_STEM_OPT: ChecklistBundle(
            visa_type=VisaType.F1_STEM_OPT,
            display_name="F-1 STEM OPT extension",
            summary="Typical items for a STEM OPT I-765 filing (24-month extension).",
            items=[
                ChecklistItem(
                    title="Form I-765",
                    detail="Use STEM-specific eligibility codes per instructions.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Filing fee(s)",
                    detail="Per current USCIS schedule.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Passport-style photo",
                    detail="USCIS specifications.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="STEM OPT I-20",
                    detail="Showing STEM OPT request; signed by you and DSO.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Degree + STEM program evidence",
                    detail="Copy of degree, transcript, and school’s STEM designation evidence as required.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Employer details on Form I-983 (Training Plan)",
                    detail="Signed by you and employer; keep updated for compliance.",
                    related_form="I-983",
                ),
                ChecklistItem(
                    title="Prior EAD copy",
                    detail="Post-completion OPT card, front and back.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="I-94 and passport/visa copies",
                    detail="Establish continuous F-1 maintenance.",
                    related_form="I-765",
                ),
            ],
        ),
        VisaType.J1: ChecklistBundle(
            visa_type=VisaType.J1,
            display_name="J-1 exchange visitor (general)",
            summary="High-level documents students and sponsors often reference; work authorization rules differ by category.",
            items=[
                ChecklistItem(
                    title="Form DS-2019",
                    detail="Signed by you and Responsible Officer; extensions or transfers as applicable.",
                    related_form="DS-2019",
                ),
                ChecklistItem(
                    title="Passport valid for travel",
                    detail="Validity rules depend on program; renew early if needed.",
                    related_form=None,
                ),
                ChecklistItem(
                    title="Proof of program funding / SEVIS fee payment",
                    detail="As required by your sponsor.",
                    related_form=None,
                ),
                ChecklistItem(
                    title="Academic training or work permission (if applicable)",
                    detail="Not all J categories allow the same employment; confirm with your sponsor before working.",
                    related_form=None,
                ),
            ],
        ),
        VisaType.H1B: ChecklistBundle(
            visa_type=VisaType.H1B,
            display_name="H-1B specialty occupation",
            summary="Common employer/petitioner-side and beneficiary documents for an H-1B petition (not a complete legal packet).",
            items=[
                ChecklistItem(
                    title="Form I-129 + H supplement",
                    detail="Petitioner completes; check current edition and filing addresses.",
                    related_form="I-129",
                ),
                ChecklistItem(
                    title="Labor Condition Application (LCA) approval (ETA-9035)",
                    detail="Public access file requirements apply to employers.",
                    related_form="ETA-9035",
                ),
                ChecklistItem(
                    title="Beneficiary resume / offer letter / job description",
                    detail="Show specialty occupation duties and qualifications.",
                    related_form="I-129",
                ),
                ChecklistItem(
                    title="Education evaluation (if degree is foreign)",
                    detail="Credential evaluation consistent with USCIS policy.",
                    related_form="I-129",
                ),
                ChecklistItem(
                    title="Passport, prior visas, I-94",
                    detail="Beneficiary identity and status history.",
                    related_form="I-129",
                ),
                ChecklistItem(
                    title="Prior approvals / I-797 copies (if any)",
                    detail="Cap-gap, extensions, amendments as applicable.",
                    related_form="I-129",
                ),
            ],
        ),
        VisaType.DACA_INITIAL: ChecklistBundle(
            visa_type=VisaType.DACA_INITIAL,
            display_name="DACA (initial request)",
            summary="Initial DACA involves both deferred action and employment authorization; follow the latest USCIS forms and instructions.",
            items=[
                ChecklistItem(
                    title="Form I-821D",
                    detail="Consideration of Deferred Action for Childhood Arrivals.",
                    related_form="I-821D",
                ),
                ChecklistItem(
                    title="Form I-765 (with appropriate category code)",
                    detail="Filed together with I-821D per instructions.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Form I-765WS (worksheet)",
                    detail="If required by current instructions.",
                    related_form="I-765WS",
                ),
                ChecklistItem(
                    title="Identity and continuous residence evidence",
                    detail="School, employment, medical, or other records as instructed.",
                    related_form="I-821D",
                ),
                ChecklistItem(
                    title="Education evidence",
                    detail="GED, diploma, enrollment records as applicable.",
                    related_form="I-821D",
                ),
                ChecklistItem(
                    title="Biometrics appointment readiness",
                    detail="ASC notice and valid ID.",
                    related_form="I-821D",
                ),
            ],
        ),
        VisaType.DACA_RENEWAL: ChecklistBundle(
            visa_type=VisaType.DACA_RENEWAL,
            display_name="DACA renewal",
            summary="Typical renewal packet elements; timelines and eligibility rules change—verify current USCIS guidance.",
            items=[
                ChecklistItem(
                    title="Form I-821D (renewal)",
                    detail="Complete renewal sections per instructions.",
                    related_form="I-821D",
                ),
                ChecklistItem(
                    title="Form I-765 renewal",
                    detail="Category code per DACA instructions.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Form I-765WS (if required)",
                    detail="Follow current edition instructions.",
                    related_form="I-765WS",
                ),
                ChecklistItem(
                    title="Copy of prior DACA approval(s) and EAD",
                    detail="Front and back of most recent EAD.",
                    related_form="I-821D",
                ),
                ChecklistItem(
                    title="Updated evidence of any criminal history changes (if any)",
                    detail="Disclosures per form instructions.",
                    related_form="I-821D",
                ),
                ChecklistItem(
                    title="Filing fee(s) or fee exemption request (if eligible)",
                    detail="Per current USCIS rules.",
                    related_form="I-821D",
                ),
            ],
        ),
        VisaType.FAMILY_ADJUSTMENT_I485: ChecklistBundle(
            visa_type=VisaType.FAMILY_ADJUSTMENT_I485,
            display_name="Family-based adjustment of status (Form I-485)",
            summary="Starter list for many family-based AOS filings; exact exhibits depend on underlying petition and grounds.",
            items=[
                ChecklistItem(
                    title="Form I-485",
                    detail="Correct edition; signed where required.",
                    related_form="I-485",
                ),
                ChecklistItem(
                    title="Form I-864 (Affidavit of Support) and financial evidence",
                    detail="Sponsor income/assets/tax transcripts as applicable.",
                    related_form="I-864",
                ),
                ChecklistItem(
                    title="Birth certificates (with certified translations if needed)",
                    detail="Establish identity and family relationships.",
                    related_form="I-485",
                ),
                ChecklistItem(
                    title="Marriage certificate / divorce decrees (if applicable)",
                    detail="Bona fide marriage evidence for spousal cases.",
                    related_form="I-485",
                ),
                ChecklistItem(
                    title="Passport biographic page, visas, I-94",
                    detail="Travel and status history.",
                    related_form="I-485",
                ),
                ChecklistItem(
                    title="Medical examination (Form I-693)",
                    detail="Sealed civil surgeon report per USCIS policy on timing.",
                    related_form="I-693",
                ),
                ChecklistItem(
                    title="Police/court records (if instructed)",
                    detail="Country-specific guidance in I-485 instructions.",
                    related_form="I-485",
                ),
                ChecklistItem(
                    title="Filing fee(s) or fee waiver request (if eligible)",
                    detail="Per USCIS fee rules.",
                    related_form="I-485",
                ),
            ],
        ),
        VisaType.ASYLUM_PENDING_EAD: ChecklistBundle(
            visa_type=VisaType.ASYLUM_PENDING_EAD,
            display_name="Asylum pending — employment authorization (general)",
            summary="Eligibility windows and categories are strict; always follow current I-765 asylum-related instructions.",
            items=[
                ChecklistItem(
                    title="Form I-765",
                    detail="Correct eligibility category for asylum-based EAD rules.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Copy of asylum application receipt or filing evidence",
                    detail="As required by instructions.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Passport-style photo and identity document copies",
                    detail="Per I-765 checklist.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="Prior EAD copies (if renewing)",
                    detail="Front and back.",
                    related_form="I-765",
                ),
                ChecklistItem(
                    title="I-94 (if available)",
                    detail="Status and entry history.",
                    related_form="I-765",
                ),
            ],
        ),
        VisaType.NATURALIZATION_N400: ChecklistBundle(
            visa_type=VisaType.NATURALIZATION_N400,
            display_name="U.S. naturalization (Form N-400)",
            summary="Common N-400 filing exhibits; interview may require originals.",
            items=[
                ChecklistItem(
                    title="Form N-400",
                    detail="Complete all parts applicable to you; sign.",
                    related_form="N-400",
                ),
                ChecklistItem(
                    title="Green card (I-551) copy — front and back",
                    detail="Lawful permanent resident evidence.",
                    related_form="N-400",
                ),
                ChecklistItem(
                    title="Passport-style photos",
                    detail="Per USCIS specifications.",
                    related_form="N-400",
                ),
                ChecklistItem(
                    title="Marital history documents (if applicable)",
                    detail="Marriage certificates, divorce decrees, spouse’s prior immigration records as needed.",
                    related_form="N-400",
                ),
                ChecklistItem(
                    title="Travel history evidence",
                    detail="Passport stamps, I-94 history, itineraries to reconcile absences.",
                    related_form="N-400",
                ),
                ChecklistItem(
                    title="Tax transcripts / selective service registration (if applicable)",
                    detail="Good moral character and statutory requirements.",
                    related_form="N-400",
                ),
                ChecklistItem(
                    title="Fee payment or fee reduction/exemption (if eligible)",
                    detail="Per USCIS fee rules.",
                    related_form="N-400",
                ),
            ],
        ),
        VisaType.OTHER: ChecklistBundle(
            visa_type=VisaType.OTHER,
            display_name="Other / not listed",
            summary="We don’t have a tailored checklist for that selection yet.",
            items=[
                ChecklistItem(
                    title="Identify your goal",
                    detail="Work permit, green card, travel document, extension, or other relief.",
                    related_form=None,
                ),
                ChecklistItem(
                    title="Find the correct USCIS form instructions",
                    detail="Use https://www.uscis.gov/forms and download the instruction PDF for your form.",
                    related_form=None,
                ),
                ChecklistItem(
                    title="Gather identity & status documents",
                    detail="Passport, I-94, prior approvals, and translations where needed.",
                    related_form=None,
                ),
                ChecklistItem(
                    title="Talk to a legal aid org or accredited representative",
                    detail="Use GET /resources for Bay Area nonprofits (this app is not legal advice).",
                    related_form=None,
                ),
            ],
        ),
    }
    return bundles[visa_type]
