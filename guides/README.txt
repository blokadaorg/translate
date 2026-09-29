Setup guides published at blokada.org/guides/.

The English files here are copied from the landing repo (guides/src/en/),
which is where they are written; don't edit them here. Run
`guides/scripts/crowdin.sh export` in the landing repo to update them, and
`guides/scripts/crowdin.sh import` to bring the translations from
build/guides/ back into the guides.

The pages contain Nunjucks tags such as {% dot %}, {% doh %} and
{{ t[lang].placeholder | safe }}, HTML blocks and relative links. Translations
must keep all of them exactly; the landing build checks this.
