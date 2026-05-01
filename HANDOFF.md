# Handoff — Amazon Eco Travellers Site

## Projeto

Site estático de ecoturismo: **Amazon Eco Travellers** — tours guiados por naturalistas na Amazônia, saindo de Manaus, Brasil.

**Arquivo único:** `C:\Users\dylan\amazon-eco-site\index.html`  
**Assets:** `assets/images/` (hero.jpg, logo.png, logo-white.png)

---

## Stack

- HTML/CSS/JS puro — tudo inline num único `index.html`
- Fontes: Playfair Display (headings, serif, itálico) + Inter (body)
- Cores: sistema OKLCH com tokens CSS (`--green`, `--green-d`, `--green-l`, `--amber`, `--terra`, `--dark`, `--warm-cream`, `--warm-white`)
- Easings customizados: `--ease: cubic-bezier(0.23, 1, 0.32, 1)` e `--ease-io: cubic-bezier(0.77, 0, 0.175, 1)`
- Ícones: Font Awesome 6.5
- Scroll reveal via IntersectionObserver + classes `.rv` / `.rv.in`

---

## Estrutura do site (seções em ordem)

1. **Header** — fixo, muda aparência ao rolar (`.scrolled`), dropdown de tours e acomodações, seletor de idioma (EN/DE/PT/ES), botão "Book Now"
2. **Hero** — fullscreen, imagem de fundo (`hero.jpg`), overlay gradiente, headline serif itálico, 2 CTAs
3. **Trust Bar** — fundo verde escuro, 5 itens: TripAdvisor, 10+ anos, guias naturalistas, tours privados/grupo, idiomas
4. **Tours** — grid 3 colunas, 5 cards:
   - Amazon Explorers (5D/4N)
   - River Explorer (5D/4N)
   - Chlorophyll (6D/5N)
   - Birdwatching (7D/6N) — "Most Popular"
   - Ecological Expedition (8D/7N)
5. **How It Works** — 3 passos numerados, grid 1fr/2fr
6. **About** — grid 2 colunas, 3 features com ícone, badge "10+ anos"
7. **Reviews** — fundo verde escuro, 3 cards — **ATENÇÃO: todos têm placeholder** `"— Add a real testimonial here"`, precisam ser substituídos por depoimentos reais
8. **CTA** — gradiente âmbar/terra, 2 botões: WhatsApp e email
9. **Footer** — 4 colunas, redes sociais, links
10. **WhatsApp Float** — botão fixo canto inferior direito

**Contatos reais no código:**
- WhatsApp: `+55 92 99132-1047`
- Instagram: `@amazonecotravellers`
- Facebook: `/EcoBiologists`
- TripAdvisor: `Attraction_Review-g303235-d15588527`

---

## O que foi feito nesta sessão

### Melhorias de motion/UI (filosofia Emil Kowalski)

Todas as mudanças foram aplicadas no `index.html`:

| Mudança | Antes | Depois |
|---------|-------|--------|
| Scroll reveal timing | `640ms, translateY(30px)` | `400ms, translateY(20px)` |
| Stagger delay `.d5` | `400ms` | `280ms` |
| Dropdown `transform-origin` | center (default) | `top center` |
| `.lnk-arr` hover | anima `gap` (não GPU) | `translateX` no ícone `<i>` |
| `.all-lnk` hover | anima `gap` (não GPU) | `translateX` no ícone `<i>` |
| `.tc-cta` hover | anima `gap` (não GPU) | `translateX` no ícone `<i>` |
| `.tc:hover` transform | sem media query | `@media (hover: hover) and (pointer: fine)` |
| `.tc:hover .tc-photo img` | sem media query | `@media (hover: hover) and (pointer: fine)` |
| `prefers-reduced-motion` | só `.rv` e `.scroll-bar` | cobre todos transforms + `.rv` vira `opacity:1` imediatamente |

---

## O que estava em andamento (PARADO AQUI)

### Skill `impeccable` — auditoria de design

A skill `impeccable` foi invocada mas ficou parada no **passo de contexto estratégico** (PRODUCT.md não existia).

O fluxo `teach` foi iniciado. Já coletei tudo que é possível inferir do código. Faltam **3 respostas do usuário** para criar o PRODUCT.md e então executar a auditoria completa:

**Pergunta 1 — Personalidade da marca (3 palavras)**
Como você quer que as pessoas se sintam ao ver o site?
Exemplos: "aventureiro, especialista, responsável" / "selvagem, autêntico, cuidadoso" / outra coisa?

**Pergunta 2 — Referências**
Algum site de turismo/viagem/outdoor que captura o feel certo para este site?
O que especificamente você gosta neles?

**Pergunta 3 — Anti-referências**
O que esse site explicitamente NÃO deve parecer?
Exemplos: "turismo de massa tipo CVC", "muito corporativo", "estética survival/caça"

---

## Próximos passos recomendados (em ordem)

1. **Responder as 3 perguntas acima** → isso permite criar o PRODUCT.md e rodar `$impeccable critique` + `$impeccable polish` no site
2. **Substituir os 3 placeholders de reviews** por depoimentos reais de clientes
3. **Adicionar imagens reais** nos cards dos tours (atualmente usam gradientes CSS como placeholder)
4. **Adicionar imagem real** na seção About (atualmente usa placeholder com ícone)
5. **Revisar links de navegação** — todos os hrefs (`/tours/amazon-explorers/`, `/accommodations/`, etc.) apontam para páginas que ainda não existem
6. **Internacionalização** — o seletor de idioma (EN/DE/PT/ES) existe visualmente mas não tem funcionalidade implementada

---

## Arquivos de contexto da IA (se precisar recriar)

As memórias do Claude estão em:
`C:\Users\dylan\.claude\projects\C--WINDOWS-system32\memory\`

- `feedback_language.md` — responder sempre em pt-br
- `feedback_design_skills.md` — em qualquer pedido de design, usar `emil-design-eng` + `impeccable`
- `project_amazon_eco_site.md` — contexto do site
- `project_skills_recentes.md` — últimas skills instaladas: `emil-design-eng` e `impeccable`

As skills estão em:
`C:\Users\dylan\.claude\skills\` (symlinks para `C:\Users\dylan\.agents\skills\`)

---

## Instrução para o próximo agente

Quando retomar:
1. Leia este arquivo
2. Leia `C:\Users\dylan\amazon-eco-site\index.html` para ver o estado atual
3. Peça ao usuário as 3 respostas pendentes (personalidade, referências, anti-referências)
4. Crie `C:\Users\dylan\amazon-eco-site\PRODUCT.md` com as respostas
5. Execute `$impeccable critique index.html` seguido de `$impeccable polish index.html`
6. Use sempre pt-br nas respostas
7. Em qualquer pedido de design, invocar `emil-design-eng` e `impeccable` automaticamente
