def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    
    # 1. Fetch Database URL from Settings / Config
    db_url = str(settings.database_url)
    
    # SQLite async -> sync compatibility handling
    if db_url.startswith("sqlite+aiosqlite://"):
        db_url = db_url.replace("sqlite+aiosqlite://", "sqlite://")
    elif db_url.startswith("postgresql+asyncpg://"):
        db_url = db_url.replace("postgresql+asyncpg://", "postgresql://")
        
    config.set_main_option("sqlalchemy.url", db_url.replace("%", "%%"))

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()