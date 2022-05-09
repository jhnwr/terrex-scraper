from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


# had issues with missing data over several models so have commented some out below

class MetaData(BaseModel):
    canonical: str
    description: str
    keywords: str
    page_title: str
    site_name: str


class Metadata(BaseModel):
    asset_usage: List[str]
    asset_category: str
    imageStyle: str
    view: str
    usageTerms: str
    sortOrder: str
    subjects: List


class ViewListItem(BaseModel):
    type: str
    source: str
    image_url: str
    metadata: Optional[Metadata]


class SizeFitBar(BaseModel):
    value: str
    markerCount: int
    selectedMarkerIndex: int


class AttributeList(BaseModel):
    sale: bool
    brand: str
    color: str
    gender: str
    outlet: bool
    sport: List[str]
    closure: List[str]
    surface: List[str]
    category: str
    sportSub: List[str]
    size_fit_bar: SizeFitBar
    collection: List[str]
    search_color: str
    base_material: List[str]
    productType: List[str]
    personalizable: bool
    isCnCRestricted: bool
    key_category_code: str
    productLineStyle: Optional[List[str]]
    mandatory_personalization: bool
    sustainability_ethics_compliance_ids: List[str]
    customizable: bool
    search_color_raw: str
    is_orderable: bool
    isWaitingRoomProduct: bool
    isInPreview: bool
    specialLaunch: bool
    special_launch_type: str
    sizeTypes: Dict[str, Any]
    is_flash: bool
    size_chart_link: str


class BreadcrumbListItem(BaseModel):
    text: str
    link: str


class PricingInformation(BaseModel):
    currentPrice: int
    standard_price: int
    standard_price_no_vat: int


class WashCareInstructions(BaseModel):
    care_instructions: List


class ProductHighlight(BaseModel):
    hcopy: str
    headline: str
    image_reference: Any


class DescriptionAssets(BaseModel):
    image_url: str
    video_url: Any
    poster_url: Any


class ProductDescription(BaseModel):
    title: str
    text: str
    subtitle: str
    usps: Optional[List[str]]
    wash_care_instructions: WashCareInstructions
    # product_highlights: Optional[List[ProductHighlight]]
    description_assets: DescriptionAssets


class PricingInformation1(BaseModel):
    standard_price: int
    sale_price: Optional[int] = None


class ProductLinkListItem(BaseModel):
    type: str
    productId: str
    name: str
    url: str
    image: str
    altImage: str
    pricing_information: PricingInformation1
    search_color: str
    default_color: str
    source: str
    available_skus: int
    badge_style: Optional[str] = None
    badge_text: Optional[str] = None


class Field(BaseModel):
    type: str
    key: str
    maxLength: int
    minLength: int
    validation: str
    textColor: str
    usesStock: bool
    stockCollection: Any


class EmbellishmentOption(BaseModel):
    position: str
    positionPrice: int
    allowChooseOwnText: bool
    fields: List[Field]


class Embellishment(BaseModel):
    embellishmentOptions: Optional[List[EmbellishmentOption]]
    articleType: str


class Model(BaseModel):
    id: str
    product_type: str
    model_number: str
    name: str
    # meta_data: MetaData
    # view_list: List[ViewListItem]
    # attribute_list: AttributeList
    # breadcrumb_list: List[BreadcrumbListItem]
    pricing_information: PricingInformation
    product_description: Optional[ProductDescription]
    # recommendationsEnabled: bool
    # product_link_list: List[ProductLinkListItem]
    # embellishment: Optional[Embellishment]
