"""Bay Area nonprofit / low-cost legal aid pointers (public directories; verify hours and eligibility)."""

from pydantic import BaseModel, Field


class LegalAidOrganization(BaseModel):
    name: str
    website: str = Field(..., description="Primary public website URL.")
    phone: str | None = Field(default=None, description="Main public line if widely published; may change.")
    counties_served: list[str] = Field(
        default_factory=list,
        description="Bay Area counties or 'Bay Area-wide' where applicable.",
    )
    services_summary: str = Field(
        ...,
        description="Short plain-language description (immigration vs general civil legal aid).",
    )


LEGAL_AID_DISCLAIMER = (
    "Listings are for orientation only. Hours, intake rules, and immigration capacity change. "
    "Call or visit the organization’s site to confirm. This app does not endorse a specific provider "
    "and does not provide legal advice."
)

# Curated from widely known Bay Area nonprofits; URLs are public homepages.
BAY_AREA_LEGAL_AID_ORGS: list[LegalAidOrganization] = [
    LegalAidOrganization(
        name="Bay Area Legal Aid",
        website="https://baylegal.org/",
        phone="(888) 382-3163",
        counties_served=["Alameda", "Contra Costa", "Marin", "Napa", "San Francisco", "San Mateo", "Santa Clara", "Solano", "Sonoma"],
        services_summary="Free civil legal help for eligible low-income residents; includes housing, public benefits, and some immigration-adjacent issues depending on office capacity.",
    ),
    LegalAidOrganization(
        name="East Bay Community Law Center (EBCLC)",
        website="https://ebclc.org/",
        phone="(510) 548-4040",
        counties_served=["Alameda", "Contra Costa"],
        services_summary="UC Berkeley–affiliated community law office; immigration legal services and policy programs among other practice areas.",
    ),
    LegalAidOrganization(
        name="Asian Law Caucus",
        website="https://www.asianlawcaucus.org/",
        phone="(415) 896-1701",
        counties_served=["San Francisco", "Bay Area-wide"],
        services_summary="Civil rights and legal services with strong immigrant-community focus (intake varies by issue and capacity).",
    ),
    LegalAidOrganization(
        name="Legal Services of Northern California",
        website="https://lsnc.net/",
        phone="(800) 870-4324",
        counties_served=["Northern California", "Bay Area (regional offices)"],
        services_summary="Broad civil legal aid for income-eligible clients; immigration services availability depends on local office.",
    ),
    LegalAidOrganization(
        name="Community Legal Services in East Palo Alto (CLSEPA)",
        website="https://clsepa.org/",
        phone="(650) 326-6440",
        counties_served=["San Mateo", "Santa Clara"],
        services_summary="Community-based legal aid serving low-income residents; immigration and tenants’ rights among program areas.",
    ),
    LegalAidOrganization(
        name="La Raza Centro Legal",
        website="https://www.larazacenter.org/",
        phone="(415) 575-5588",
        counties_served=["San Francisco", "Bay Area-wide"],
        services_summary="Immigrant workers’ rights, housing, and related legal services with Spanish-language capacity.",
    ),
    LegalAidOrganization(
        name="Pangea Legal Services",
        website="https://pangealegal.org/",
        phone=None,
        counties_served=["San Francisco", "Oakland", "Bay Area-wide"],
        services_summary="Nonprofit focused on deportation defense and immigrant justice (capacity and intake rules vary).",
    ),
    LegalAidOrganization(
        name="Catholic Charities East Bay — Immigration Legal Services",
        website="https://www.cceb.org/our-programs/immigration-legal-services/",
        phone="(510) 768-3100",
        counties_served=["Alameda", "Contra Costa"],
        services_summary="Department of Justice–recognized program offering immigration consultations and representation to eligible clients.",
    ),
    LegalAidOrganization(
        name="Catholic Charities San Francisco — Immigration Legal Services",
        website="https://www.ccsf.org/immigration-legal-services/",
        phone="(415) 972-1312",
        counties_served=["San Francisco", "San Mateo", "Marin"],
        services_summary="Immigration legal services including naturalization and family cases for eligible clients.",
    ),
    LegalAidOrganization(
        name="International Institute of the Bay Area (IIBA)",
        website="https://www.iiba.org/",
        phone="(510) 451-2846",
        counties_served=["Alameda", "Contra Costa", "San Francisco", "San Mateo", "Santa Clara", "Marin"],
        services_summary="Immigration legal services, citizenship workshops, and education programs across multiple Bay Area offices.",
    ),
    LegalAidOrganization(
        name="API Legal Outreach",
        website="https://www.apilegal.org/",
        phone="(415) 567-6255",
        counties_served=["San Francisco", "San Mateo", "Santa Clara"],
        services_summary="Legal services for low-income Asian and Pacific Islander communities; immigration and seniors’ law among programs.",
    ),
    LegalAidOrganization(
        name="ALAS Immigrant Family Legal Services",
        website="https://www.alasfe.org/",
        phone="(650) 560-0204",
        counties_served=["San Mateo", "Coastside"],
        services_summary="Immigration legal services and family support for Coastside and San Mateo County residents.",
    ),
    LegalAidOrganization(
        name="Canal Alliance (Marin)",
        website="https://canalalliance.org/",
        phone="(415) 454-2640",
        counties_served=["Marin"],
        services_summary="Immigrant services, education, and legal immigration program for Marin County residents (eligibility applies).",
    ),
    LegalAidOrganization(
        name="Dolores Street Community Services — Immigration Center",
        website="https://www.dscs.org/programs/immigration-center/",
        phone="(415) 282-6209",
        counties_served=["San Francisco"],
        services_summary="San Francisco–based services including legal orientation and representation programs for immigrants.",
    ),
    LegalAidOrganization(
        name="Jewish Family and Community Services East Bay — Immigration Legal Services",
        website="https://jfcs-eastbay.org/immigration-legal-services/",
        phone="(510) 704-7475",
        counties_served=["Alameda", "Contra Costa"],
        services_summary="Nonprofit immigration legal services for refugees, asylees, and other eligible community members.",
    ),
]
