export default {
    // Those are all languages that will actually be exported.
    "langs": ["pl", "de", "es", "it", "hi", "ru", "bg", "tr", "ja", "id", "cs", "zh-Hant", "ar", "fi", "ro", "pt-BR", "fr", "hu", "nl", "sv"],
    // Those names will be replaced android exports (the rest from above wont be changed but will be exported).
    "langs-android": {
        "id": "in",
        "zh-Hant": "zh",
        "pt-BR": "b+pt+BR"
    },
    "langs-android-res": {
        "pl": "pl-rPL",
        "de": "de-rDE",
        "es": "es-rES",
        "it": "it-rIT",
        "hi": "hi-rIN",
        "ru": "ru-rRU",
        "bg": "bg-rBG",
        "tr": "tr-rTR",
        "ja": "ja-rJP",
        "id": "in-rID",
        "cs": "cs-rCZ",
        "zh-Hant": "zh-rTW",
        "ar": "ar-rSA",
        "fi": "fi-rFI",
        "ro": "ro-rRO",
        "pt-BR": "pt-rBR",
        "fr": "fr-rFR",
        "hu": "hu-rHU",
        "nl": "nl-rNL",
	    "sv": "sv-rSE"
    },
    // Those names will be replaced for web exports
    "langs-web4": {
        "pl": "pl_PL",
        "de": "de_DE",
        "es": "es_ES",
        "it": "it_IT",
        "hi": "hi_IN",
        "ru": "ru_RU",
        "bg": "bg_BG",
        "tr": "tr_TR",
        "ja": "ja_JP",
        "id": "id_ID",
        "cs": "cs_CZ",
        "zh-Hant": "zh_TW",
        "ar": "ar_SA",
        "fi": "fi_FI",
        "ro": "ro_RO",
        "pt-BR": "pt_BR",
        "fr": "fr_FR",
        "hu": "hu_HU",
        "nl": "nl_NL",
	    "sv": "sv_SE"
    },
    // Those names will be replaced for arb exports
    // For flutter we don't export country scripts, since it requires a silly "fallback" rule
    // T export "pt-BR" and "pt-PT" we'd need to also export "pt".
    // Currently we simplify this since we don't export two languages like this yet...
    "langs-arb": {
        "zh-Hant": "zh",
        "pt-BR": "pt"
    },
}
