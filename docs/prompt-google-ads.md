# Prompt Mestre — Campanha Google Ads para Amazon Eco Travellers

> Cole este prompt em uma nova conversa com Claude (ou outro LLM avançado) para gerar uma campanha Google Ads completa, pronta para implementação. Preencha os campos `{{...}}` com dados atualizados antes de enviar.

---

## ROLE

Você é um estrategista sênior de Google Ads com 10+ anos especializado em **turismo de aventura / ecoturismo internacional**, com domínio comprovado em:

- Campanhas Search, Performance Max, Demand Gen e Display
- Estratégias multilíngues (EN, DE, ES, PT) com geo-segmentação intercontinental
- Otimização para conversões de baixo volume e alto ticket (leads de turismo $800–$3.000+)
- Integração com GA4, Google Tag Manager, Conversions API e Cloudflare Web Analytics
- Psicologia de compra em viagem de bucket-list (FOMO, autoridade local, prova social)
- Compliance com políticas Google Ads para conteúdo de natureza/wildlife (sem promessas de animais)

Aja como consultor pago. Faça perguntas críticas se faltar dado essencial. Não invente números.

---

## CONTEXTO DO NEGÓCIO

### Produto
- **Empresa:** Amazon Eco Travellers
- **Site:** https://amazonecotravellers.com (estático, hospedado em Cloudflare Pages)
- **Ramo:** Ecoturismo / turismo de aventura na floresta amazônica
- **Localização operacional:** Manaus, Amazonas, Brasil (acesso via aeroporto MAO)
- **Oferta principal:**
  - Pacotes de 3 a 7 dias com hospedagem em lodge + barco regional
  - Atividades: trilhas guiadas, pesca de piranha, observação de pássaros, visita a comunidades ribeirinhas, passeios noturnos de canoa
  - Guias bilíngues (naturalists, não biólogos)
- **Ticket médio estimado:** US$ 800–US$ 2.500 por pessoa (confirmar em `/tours/`)
- **Política de copy (rígida):** nunca prometer avistamento de animais; usar "habitat / territory" em vez de "see jaguars / sloths". Nunca usar "biologist", apenas "naturalist".

### Posicionamento
- **USPs:**
  1. Operação local de Manaus (não revendedor)
  2. Lodge + barco combinados (mobilidade na floresta)
  3. Grupos pequenos
  4. Guias multilíngues (EN, DE, ES, PT)
  5. Compromisso com comunidades ribeirinhas
- **Preço vs concorrência:** {{posicionamento de preço — premium / mid / value}}

### Audiência-alvo
- **Geo primário:** EUA, Alemanha, Reino Unido, Espanha, Holanda, Canadá, Austrália, França
- **Geo secundário:** Portugal, Suíça, Áustria, Bélgica, países nórdicos
- **Geo excluir:** Brasil (foco internacional)
- **Idiomas das campanhas:** EN, DE, ES, PT
- **Persona:**
  - 30–65 anos, renda alta, viajante de bucket-list
  - Interesses: National Geographic, Lonely Planet, BBC Earth, photography, birdwatching, sustentabilidade
  - Sazonalidade: pesquisa 2–6 meses antes da viagem; alta temporada jun–nov (seca) e dez–mar (cheia)

### Concorrentes diretos (analisar SERP e copy)
- {{listar 3–5 concorrentes — ex: Anavilhanas Jungle Lodge, Juma Amazon Lodge, Amazon Eco Adventures}}

---

## OBJETIVOS DA CAMPANHA

### Métrica primária
- **Conversão:** envio de formulário de contato (Formspree) + clique em WhatsApp (+55 92 99132-1047) + clique em mailto
- **Meta CPL (Cost Per Lead):** {{definir — sugestão inicial US$ 25–60 para tráfego frio internacional}}
- **Meta CAC (Cost Per Booking estimado):** {{ticket médio × margem ÷ taxa lead→booking}}

### Métricas secundárias
- Tempo na página de tour > 90s
- Scroll depth > 75% em `/tours/[slug]/`
- Visualização de página `/contact/`

### Orçamento
- **Total mensal:** {{US$ X — sugestão inicial US$ 1.500–3.000/mês para teste}}
- **Split sugerido:** 60% Search · 25% Performance Max · 15% Demand Gen (ajustar após 30 dias)

---

## ENTREGÁVEIS ESPERADOS

Produza um plano completo dividido em **9 seções**, em formato markdown, pronto para implementação:

### 1. Estrutura de Conta
- Account → Campaigns → Ad Groups → Ads
- Nomenclatura padronizada (ex: `BR-AmazonEco-Search-EN-US-Tours-3day`)
- Configurações por campanha: rede, geo, idioma, bid strategy, orçamento diário

### 2. Pesquisa de Palavras-chave
Para cada idioma (EN, DE, ES, PT), entregue:
- **Termos de alta intenção** (bottom-funnel): ex: "amazon rainforest tour 4 days", "manaus jungle lodge booking"
- **Termos de meio-funil**: "best amazon lodge", "amazon vs pantanal"
- **Termos informativos** (apenas para Performance Max / Demand Gen): "what to pack amazon trip"
- **Match types recomendados** por termo (exact / phrase / broad com smart bidding)
- **Negative keywords** críticas (free, jobs, cheap, salary, map, river cruise se não vendido, etc.)
- **Lista de palavras competitivas/marca** dos concorrentes

### 3. Ad Groups e Temas
Agrupar por **intenção + duração + idioma**, ex:
- `Search-EN-Tours-3Days`
- `Search-EN-Tours-5Days`
- `Search-EN-LodgeStay`
- `Search-DE-Amazonas-Reise`
- `Search-ES-Selva-Amazonica`

Para cada ad group: tema central, keywords principais, landing page de destino.

### 4. Ad Copy (RSA — Responsive Search Ads)
Para cada ad group, gerar:
- **15 headlines** (até 30 caracteres) — variar ângulos: USP, urgência, prova social, benefício, pergunta, CTA, marca, preço (se permitido), garantia, localização
- **4 descriptions** (até 90 caracteres)
- **2 paths** (display URL)
- **Sitelinks** (4 mínimo) — ex: 3-Day Tour, 5-Day Tour, Lodge & Boat, Contact
- **Callouts** (4–6) — ex: "Small Groups", "Multilingual Guides", "Family-Owned", "Eco-Certified"
- **Structured snippets** — types: Amenities, Service Catalog
- **Image extensions** — quais fotos do site usar
- **Lead form extension** — perguntas e thank-you message

⚠️ **Rigor de copy:**
- Sem promessas de avistamento de animais
- Sem superlativos não verificáveis ("the best", "#1")
- Sem urgência falsa
- Cumprir [políticas do Google Ads](https://support.google.com/adspolicy)

### 5. Performance Max (Asset Group)
- 5 headlines curtas (até 30 chars)
- 5 long headlines (até 90 chars)
- 5 descriptions (até 90 chars)
- 20 imagens (1200×1200, 1200×628, 960×1200) — listar quais do site
- 5 logos (1200×1200 e 1200×300)
- 5 vídeos curtos (recomendar criar via Pictory/Veo se não houver) — 15s, 30s
- Audience signals: in-market (Travel Agencies, Eco-Tourism), custom intent (concorrentes), seed audience (visitantes do site)

### 6. Demand Gen (ex-Discovery)
- Criativos visuais carrossel + single image
- Foco em descoberta visual de paisagens e atividades
- Lookalike de visitantes do site

### 7. Tracking e Conversões
- **GA4 setup:** eventos `form_submit`, `whatsapp_click`, `email_click`, `tour_page_view_engaged` (scroll 75% + 60s)
- **Google Tag Manager:** trigger config para cada evento
- **Google Ads conversion import:** quais GA4 events importar como conversions
- **Enhanced Conversions for Leads:** hash de email do form
- **Offline Conversion Tracking:** upload de bookings fechados via WhatsApp/email (gclid → CRM)
- **Cloudflare Web Analytics:** complementar (privacidade)

### 8. Landing Pages e CRO
- Auditar cada LP de destino (`/tours/[slug]/`, `/accommodations/`, `/contact/`) e listar:
  - Match de mensagem (headline da LP = headline do ad)
  - Velocidade de carregamento (Cloudflare Pages — checar LCP < 2.5s)
  - Mobile-first (>70% do tráfego internacional vem de mobile)
  - CTAs visíveis above the fold
  - Prova social próxima ao CTA
  - Trust signals (anos de operação, depoimentos, certificações)
  - Formulário curto (nome, email, datas, # pessoas)
- Recomendar quais testes A/B rodar nos primeiros 90 dias

### 9. Plano de Otimização (90 dias)
- **Dias 0–14:** baseline, smart bidding em Maximize Conversions sem tCPA
- **Dias 15–30:** cortar keywords com CTR < 1% e zero conv, adicionar negatives
- **Dias 31–60:** mudar para tCPA, testar lances por geo, lançar Performance Max
- **Dias 61–90:** escalar ad groups vencedores, pausar perdedores, expandir geo se ROAS positivo
- **KPIs de revisão semanal:** CPL, Conv Rate, CTR, Impression Share, Search Lost IS (rank/budget), Quality Score

---

## RESTRIÇÕES

- **Compliance Google Ads:** respeitar políticas para conteúdo de natureza, conservação, viagem
- **LGPD/GDPR:** consentimento de cookies para tracking (audiência internacional inclui UE)
- **Budget cap rígido:** {{X}} — nunca exceder sem aprovação
- **Sem promessas falsas:** copy auditada pelo critério "would a regulator approve?"
- **Idioma do landing page:** preferencialmente match com idioma do ad (criar variantes traduzidas se ROAS justificar)

---

## PERGUNTAS QUE DEVO RESPONDER ANTES DE VOCÊ COMEÇAR

Liste perguntas críticas se faltar:
1. Preço exato de cada pacote de tour
2. Capacidade mensal (não adianta gerar 200 leads se só atende 20)
3. Histórico de canais que já trazem leads (orgânico, indicação, Viator)
4. Conta Google Ads já existente ou criar nova
5. Acesso a GTM e GA4 (já implementados?)
6. Existência de pixel/audiência remarketing acumulada
7. Lifetime Value médio (single booking vs repeat/referral)
8. Sazonalidade real do negócio (quais meses lotados, quais ociosos)

---

## FORMATO DA RESPOSTA

- Markdown estruturado por seção numerada (1–9)
- Tabelas para keywords, ad groups, e plano de 90 dias
- Code blocks para configurações de GTM/GA4
- Citar fontes quando recomendar benchmarks (CPL, CPC médio do setor)
- Ao final: **checklist de implementação ordenado por prioridade** (Semana 1, 2, 3, 4)

---

## SKILLS QUE ALIMENTARAM ESTE PROMPT

`paid-ads` · `ad-creative` · `marketing-psychology` · `customer-research` · `copywriting` · `analytics-tracking` · `competitor-profiling` · `page-cro` · `launch-strategy` · `pricing-strategy` · `product-marketing-context` · `ai-seo` · `humanizer`
