# Customizing FastAPI Documentation

The web-dlp API documentation is fully customizable. Here are the options:

## Current Customizations Applied

### 1. **Enhanced Description** 
- Added emojis and formatting
- Listed key features
- Included quick start guide

### 2. **Swagger UI Theme**
- Syntax highlighting: Monokai theme
- Auto-expand endpoints
- Search filter enabled
- Schemas section hidden by default

### 3. **Metadata**
- Contact information
- License details
- Version tracking

## Additional Customization Options

### Change Color Scheme

Add this to `main.py` after the app initialization:

```python
from fastapi.openapi.docs import get_swagger_ui_html

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Docs",
        swagger_css_url="/static/custom-swagger.css",  # Your custom CSS
    )
```

### Add Custom CSS

Create `app/static/custom-swagger.css`:

```css
/* Dark theme with custom colors */
.swagger-ui {
    font-family: 'Inter', sans-serif;
}

.swagger-ui .topbar {
    background-color: #1a1a2e;
    border-bottom: 2px solid #16213e;
}

.swagger-ui .info .title {
    color: #00d4ff;
}

.swagger-ui .opblock-summary {
    background-color: #0f3460;
    border-color: #16213e;
}

.swagger-ui .opblock.opblock-get .opblock-summary {
    border-left-color: #61dafb;
}

.swagger-ui .opblock.opblock-post .opblock-summary {
    border-left-color: #49cc90;
}

.swagger-ui .btn.execute {
    background-color: #00d4ff;
    color: #1a1a2e;
    border: none;
}
```

### Use ReDoc Instead

ReDoc offers a cleaner, modern alternative:

```python
from fastapi.openapi.docs import get_redoc_html

@app.get("/", include_in_schema=False)
async def root():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="web-dlp API Documentation"
    )
```

### Add Custom Logo

```python
app = FastAPI(
    title="web-dlp API",
    # ... other params
    swagger_ui_parameters={
        "customSiteTitle": "web-dlp API",
        "customfavIcon": "https://your-domain.com/favicon.ico",
    }
)
```

### Different Syntax Themes

Available themes:
- `"agate"` - Dark with orange highlights
- `"arta"` - Dark blue theme
- `"monokai"` - Popular dark theme (default)
- `"nord"` - Arctic-inspired palette
- `"obsidian"` - Pure black theme
- `"tomorrow-night"` - Soft dark theme

Change in `swagger_ui_parameters`:
```python
"syntaxHighlight.theme": "nord"
```

### Add Examples to Endpoints

Already done! See the docstrings in each endpoint function.

### Disable Documentation Entirely

For production (not recommended):
```python
app = FastAPI(docs_url=None, redoc_url=None)
```

## Current Documentation URLs

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## Testing Your Changes

1. Restart the API server
2. Visit `http://localhost:8000/docs`
3. See your customizations!

The documentation is automatically updated based on:
- Function docstrings
- Type hints
- Pydantic models
- Route decorators
