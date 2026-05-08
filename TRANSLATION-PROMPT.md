# Prompt: i18n Completo — Amazon Eco Travellers

## Contexto do Projeto

Site estático em `C:\Users\dylan\amazon-eco-site`.
Repositório Git: branch `master`, remote `origin/master`.
12+ páginas HTML. Sistema i18n já implementado: `assets/js/i18n.js`.
4 idiomas: **EN · DE · ES · PT**.

---

## Segurança Git — FAÇA ISSO PRIMEIRO

Antes de qualquer alteração, crie um commit de checkpoint:

```bash
cd C:\Users\dylan\amazon-eco-site
git status
git add -A
git commit -m "checkpoint: antes de tradução [NOME-DA-PÁGINA]"
```

Isso garante que `git checkout -- .` ou `git reset --hard HEAD~1` restaura o estado anterior. Nunca pule esse passo.

---

## Estado Atual das Traduções

### Páginas com i18n COMPLETO (não mexer):
| Página | Namespace no i18n.js |
|--------|---------------------|
| `index.html` | `home` |
| `tours/index.html` | `tl` |
| `about/index.html` | `about` |
| `accommodations/index.html` | `ac` |
| `tours/amazon-explorers/index.html` | `amazon-explorers` |
| `tours/birdwatching/index.html` | `birdwatching` |
| `tours/amazon-lodge/index.html` | `amazon-lodge` |
| `tours/river-explorer/index.html` | `river-explorer` |

Namespaces compartilhados já traduzidos (usados por todas as páginas): `nav`, `mob`, `footer`, `common`.

### Páginas que AINDA PRECISAM de i18n completo:
- `blog/index.html`
- `contact/index.html`
- `faq/index.html`
- `gallery/index.html`
- `reviews/index.html`
- `tours/amazon-complete/index.html`
- `tours/amazon-expedition/index.html`
- `tours/anavilhanas/index.html`
- `tours/ariau-river/index.html`
- `tours/chlorophyll/index.html`
- `tours/ecological-expedition/index.html`
- `tours/jungle-lodge-3days/index.html`
- `tours/jungle-retreat/index.html`
- `tours/pink-dolphins/index.html`
- `tours/presidente-figueiredo/index.html`

---

## Como o Sistema i18n Funciona

### Arquivo central: `assets/js/i18n.js`

Objeto `T` com 4 idiomas → namespaces → chaves:

```js
var T = {
    en: {
        nav: { tours: 'Tours', ... },
        mob: { ... },
        footer: { ... },
        common: { view_tour: 'View Tour', ... },
        home: { hero_title: 'Amazon tours...', ... },
        "river-explorer": {
            stat1_lbl: 'Duration',
            stat1_val: '5 Days / 4 Nights',
            intro: 'The <strong>River Explorer</strong> is...',
            ...
        }
    },
    de: { ... mesma estrutura ... },
    es: { ... mesma estrutura ... },
    pt: { ... mesma estrutura ... }
}
```

O script lê `localStorage('lang')` ou padrão `'en'` e substitui todos os elementos marcados.

---

## Regras de Marcação HTML

### Texto simples (sem HTML interno):
```html
<p data-i18n="namespace.chave">Texto em inglês</p>
<h1 data-i18n="namespace.chave">Título</h1>
<span data-i18n="namespace.chave">Rótulo</span>
```

### Texto com HTML interno (bold, em, tags, ícones Font Awesome):
```html
<p data-i18n-html="namespace.chave">Texto com <strong>negrito</strong> ou <em>itálico</em></p>
<div data-i18n-html="namespace.chave"><i class="fa-solid fa-water"></i> Label com ícone</div>
```

**Regra crítica:** Use `data-i18n-html` quando o conteúdo original tiver qualquer tag HTML (`<strong>`, `<em>`, `<br>`, `<i>`, etc.). Use `data-i18n` para texto puro.

### O que NÃO traduzir:
- Atributos `href`, `src`, `alt`, `title`
- Metadados SEO (`<title>`, `<meta description>`, Open Graph) — permanecem em EN
- Classes CSS e IDs
- Texto dentro de `<script>` e `<style>`
- Botões de WhatsApp (o URL permanece)
- Endereços de email

---

## Convenção de Nomes de Namespace

| Tipo de página | Convenção | Exemplo |
|---------------|-----------|---------|
| Tour multi-day | slug da URL | `river-explorer`, `amazon-lodge`, `birdwatching` |
| Tour day excursion | slug da URL | `pink-dolphins`, `ariau-river`, `anavilhanas` |
| Página institucional | abreviação curta | `home`, `about`, `ac`, `tl`, `faq`, `blog` |

---

## Passo a Passo Para Cada Página

### 1. Ler a página alvo

```
Read: C:\Users\dylan\amazon-eco-site\[caminho]/index.html
```

### 2. Identificar todos os elementos de texto traduzíveis

Varrer o HTML e listar todos os elementos com texto visível ao usuário. Ignorar nav/footer (já têm `data-i18n` dos commits anteriores).

### 3. Definir o namespace

Usar o slug da URL da página. Ex: `tours/pink-dolphins/` → namespace `pink-dolphins`.

### 4. Criar as chaves EN

Para cada elemento, criar uma chave descritiva no padrão `namespace.chave_descritiva`.  
Exemplos reais:
- `river-explorer.stat1_lbl` → `"Duration"`
- `river-explorer.d1_name` → `"Amazon Wildlife — MUSA Tower & Rio Negro"`
- `river-explorer.intro` → `"The <strong>River Explorer</strong> is our river-focused..."` (usa `data-i18n-html`)

### 5. Traduzir para DE, ES, PT

**Regras de copy obrigatórias:**
- Sem promessas de avistamento de animais → usar "habitat", "territory" (ex: "pink dolphin habitat", não "swim with pink dolphins")
- Sem "biologist" → usar "naturalist"
- Tom: poético, evocativo, não commercial. Veja o DE como referência de qualidade.

**Referências de estilo por idioma:**
- DE: longa, literária, detalhada (ver `about` namespace no DE do i18n.js)
- ES: fluida, calorosa, descritiva
- PT: natural, não literal, soa como português nativo do Brasil

### 6. Adicionar `data-i18n` / `data-i18n-html` no HTML

Marcar cada elemento. O conteúdo original (EN) permanece como fallback visible no HTML. Ex:

```html
<!-- ANTES -->
<p class="ts-label">Duration</p>

<!-- DEPOIS -->
<p class="ts-label" data-i18n="pink-dolphins.stat1_lbl">Duration</p>
```

### 7. Inserir o namespace novo no i18n.js

**Localização exata no arquivo:** Abrir `assets/js/i18n.js` e adicionar o novo namespace **dentro de cada idioma** (`en`, `de`, `es`, `pt`), seguindo a ordem dos idiomas já existentes.

**IMPORTANTE:** Não sobrescrever o arquivo inteiro. Usar Edit para inserir apenas o namespace novo dentro de cada bloco de idioma existente.

Estrutura de inserção:

```js
// No bloco en: { ... }, adicionar após o último namespace existente:
"pink-dolphins": {
    stat1_lbl: 'Duration',
    stat1_val: 'Full Day',
    hero_h: 'Pink Dolphins & Anavilhanas',
    intro: 'A <strong>full-day expedition</strong> on the Rio Negro...',
    ...
},

// Repetir para de: {}, es: {}, pt: {}
```

### 8. Testar visualmente

Abrir o HTML no browser, clicar nos botões EN → DE → ES → PT no nav e verificar se todos os textos mudam corretamente.

### 9. Commit

```bash
git add tours/pink-dolphins/index.html assets/js/i18n.js
git commit -m "feat: i18n completo em tours/pink-dolphins

Adiciona data-i18n/data-i18n-html em todos os elementos de texto do
tour Pink Dolphins e insere namespace pink-dolphins nos 4 idiomas
(EN, DE, ES, PT) em assets/js/i18n.js."
```

---

## Como Reverter se Algo Der Errado

### Ver o estado antes da alteração:
```bash
git log --oneline -10
```

### Descartar mudanças não commitadas:
```bash
git checkout -- tours/pink-dolphins/index.html
git checkout -- assets/js/i18n.js
```

### Voltar ao commit anterior (se já commitou):
```bash
git reset --hard HEAD~1
```

### Voltar a um commit específico:
```bash
git reset --hard [hash-do-commit]
```

---

## Exemplo Completo: Padrão de um Tour Page

Veja `tours/river-explorer/index.html` como referência canônica de como uma página tour deve ficar após a tradução. Commit de referência: `854b63a`.

Para ver o diff exato do que foi feito:
```bash
git show 854b63a
```

Para ver o diff do amazon-lodge:
```bash
git show be0b730
```

---

## Checklist Por Página

- [ ] Checkpoint git antes de começar
- [ ] Namespace definido (slug da URL)
- [ ] Todos os textos do `<main>` marcados com `data-i18n` ou `data-i18n-html`
- [ ] Nav e footer: já têm `data-i18n` (não duplicar)
- [ ] Chaves EN criadas com nomes descritivos
- [ ] Traduções DE criadas (qualidade literária)
- [ ] Traduções ES criadas
- [ ] Traduções PT criadas (PT-BR natural)
- [ ] Copy: sem promessas de animais, sem "biologist"
- [ ] Namespace inserido nos 4 idiomas no `i18n.js`
- [ ] Teste visual no browser (4 idiomas)
- [ ] Commit com mensagem padrão

---

## Arquivos Críticos

| Arquivo | Descrição |
|---------|-----------|
| `assets/js/i18n.js` | Objeto central com todas as traduções — único arquivo JS do sistema |
| `assets/js/main.js` | Scripts gerais — NÃO mexer para tradução |
| `assets/css/main.css` | CSS global — NÃO mexer para tradução |

---

## Contato (para usar nos textos)
- WhatsApp: `https://wa.me/5592991321047`
- Email: `info@amazonecotravellers.com`
