@echo off
setlocal enabledelayedexpansion

:: ============================================================
:: CONFIGURACION
:: ============================================================
set "PREFIJO=SCavanna-"
set "MAX_DEPTH=5"
set "SCRIPT_DIR=%~dp0"

:: ============================================================
:: FASE 1: CONTEO Y PREVIEW
:: ============================================================
set /a TOTAL=0
set /a YA_TIENE=0

call :ContarDir "%SCRIPT_DIR%" 0

echo.
echo ================================================
echo  RENOMBRAR ARCHIVOS - Agregar Prefijo
echo ================================================
echo.
echo  Prefijo           : %PREFIJO%
echo  Directorio base   : %SCRIPT_DIR%
echo  Profundidad maxima: %MAX_DEPTH% niveles
echo  Archivos a renombrar : %TOTAL%
echo  Ya tienen prefijo    : %YA_TIENE%
echo.

if %TOTAL% EQU 0 (
    echo  No se encontraron archivos JPG/JPEG/PNG para renombrar.
    echo.
    pause
    exit /b 0
)

echo  NOTA: Se preservan fechas de creacion y modificacion.
echo        El comando REN no modifica metadatos del archivo.
echo.
set /p "CONFIRMAR=  Desea continuar? (S/N): "
if /i not "%CONFIRMAR%"=="S" (
    echo.
    echo  Operacion cancelada.
    pause
    exit /b 0
)

:: ============================================================
:: FASE 2: RENOMBRAR
:: ============================================================
echo.
echo  Procesando...
echo  ------------------------------------------------

set /a RENOMBRADOS=0
set /a ERRORES=0

call :ProcesarDir "%SCRIPT_DIR%" 0

echo.
echo ================================================
echo  RESUMEN
echo ================================================
echo  Renombrados : %RENOMBRADOS%
echo  Errores     : %ERRORES%
echo  Omitidos    : %YA_TIENE% (ya tenian prefijo)
echo ================================================
echo.
pause
exit /b 0

:: ============================================================
:: SUBRUTINA: Contar archivos (preview)
:: ============================================================
:ContarDir
set "C_DIR=%~1"
set /a C_DEPTH=%2

if %C_DEPTH% GEQ %MAX_DEPTH% exit /b

pushd "%C_DIR%" 2>nul || exit /b

for %%F in (*.jpg *.jpeg *.png) do (
    set "C_NAME=%%~nxF"
    echo !C_NAME! | findstr /b /i "%PREFIJO%" >nul
    if !errorlevel! EQU 0 (
        set /a YA_TIENE+=1
    ) else (
        set /a TOTAL+=1
    )
)

set /a C_NEXT=C_DEPTH+1
for /d %%D in (*) do (
    call :ContarDir "%%~fD" !C_NEXT!
)

popd
exit /b

:: ============================================================
:: SUBRUTINA: Procesar y renombrar
:: ============================================================
:ProcesarDir
set "P_DIR=%~1"
set /a P_DEPTH=%2

if %P_DEPTH% GEQ %MAX_DEPTH% exit /b

pushd "%P_DIR%" 2>nul || exit /b

for %%F in (*.jpg *.jpeg *.png) do (
    set "P_NAME=%%~nxF"
    echo !P_NAME! | findstr /b /i "%PREFIJO%" >nul
    if !errorlevel! EQU 0 (
        echo  [OMITIDO] !P_NAME!
    ) else (
        ren "%%F" "%PREFIJO%!P_NAME!"
        if !errorlevel! EQU 0 (
            set /a RENOMBRADOS+=1
            echo  [OK] !P_NAME! -^> %PREFIJO%!P_NAME!
        ) else (
            set /a ERRORES+=1
            echo  [ERROR] !P_NAME!
        )
    )
)

set /a P_NEXT=P_DEPTH+1
for /d %%D in (*) do (
    call :ProcesarDir "%%~fD" !P_NEXT!
)

popd
exit /b
