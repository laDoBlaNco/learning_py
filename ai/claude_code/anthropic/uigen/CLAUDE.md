# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: UIGen

An AI-powered React component generator with live preview. Users describe components in natural language, Claude generates them via the Anthropic API, and results render live in an iframe with a Monaco editor for refinement.

**Stack:** Next.js 15 (App Router), React 19, TypeScript, Tailwind CSS v4, Prisma + SQLite, Vercel AI SDK, shadcn/ui

## Commands

All commands run from `uigen/`:

```bash
npm run setup       # First-time setup: install deps + Prisma generate + migrate
npm run dev         # Dev server with Turbopack
npm run build       # Production build
npm run test        # Run Vitest suite
npm run db:reset    # Wipe and re-seed database
```

Run a single test file:
```bash
npx vitest run src/lib/__tests__/file-system.test.ts
```

## Environment

Requires `uigen/.env`:
```
ANTHROPIC_API_KEY=sk-ant-...
```

## Architecture

### AI Generation Flow

1. User sends message → `POST /api/chat` (`src/app/api/chat/route.ts`)
2. Route calls Claude via Vercel AI SDK with the system prompt from `src/lib/prompts/generation.tsx`
3. Claude uses two tools (`str_replace_editor`, `file_manager`) to write/edit files in the virtual file system
4. Streaming response goes back to the client; on finish, the project is auto-saved to the database
5. The `PreviewFrame` component detects file changes and re-compiles JSX via Babel standalone in the iframe

### Virtual File System

All generated component files live in memory (`src/lib/file-system.ts`) — nothing is written to disk. The file tree is serialized to JSON for database persistence. `/App.jsx` is always the preview entry point.

### AI Tools (`src/lib/tools/`)

- **`file_manager`** — create/read/update/delete virtual files and directories
- **`str_replace_editor`** — targeted string replacement within file content (used for incremental edits)

### State Management

- `src/lib/contexts/ChatContext.tsx` — message history, streaming state, current project
- `src/lib/contexts/FileSystemContext.tsx` — virtual file tree, active file, editor operations

### Auth

JWT sessions via `jose` stored in HTTP-only cookies (7-day expiry). Anonymous users are fully supported; projects save to DB only for authenticated users. See `src/lib/auth.ts` and `src/actions/index.ts`.

### Database

Prisma with SQLite. Two models: `User` (email/password) and `Project` (name, userId, messages JSON, data JSON). Run `npx prisma studio` to inspect data.

### Path Alias

`@/*` maps to `src/*` (configured in `tsconfig.json`).
