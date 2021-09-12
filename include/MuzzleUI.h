#ifndef MUZZLEUI_H
#define MUZZLEUI_H

#include <Muzzle.h>
#include <stdio.h>
#include <stdbool.h>

#define MZ_UI_COLLIDER_BUFFER_AREA 5

#define MuzzleUI_NewButton(x, y, width, height, disabled) (MuzzleUI_Button){(rectangle){x, y, width + MZ_UI_COLLIDER_BUFFER_AREA, height + MZ_UI_COLLIDER_BUFFER_AREA}, disabled}
#define MZUI_UTIL_NEWVEC2(x,y) (vec2){x,y}
#define MZUI_UTIL_NEWREC(x,y,w,h) (rectangle){x,y,w,h}

/*** ENUMS ***/

enum MUZZLEUI_BUTTON_STATUS
{
    REGULAR = 0,
    DISABLED = 1,
    HOVER,
    PRESSED
};

/*** ENUMS ***/

/*** STRUCTS ***/

struct _muzzle_ui_style_border
{
    int use;
    int size;
    tint color;
};

struct _muzzle_ui_style_object_status
{
    struct _muzzle_ui_style_border border;
    tint color;
};

struct _muzzle_ui_style_rectangle
{
    struct _muzzle_ui_style_object_status pressed;
    struct _muzzle_ui_style_object_status hover;
    struct _muzzle_ui_style_object_status disabled;
    struct _muzzle_ui_style_object_status regular;
};

typedef struct _muzzle_ui_style
{
    struct _muzzle_ui_style_rectangle rectangle;
    
} MuzzleUI_Style;

typedef struct _muzzle_ui_button
{
    rectangle collider;
    enum MUZZLEUI_BUTTON_STATUS status;
} MuzzleUI_Button;

/*** STRUCTS ***/

/*** GLOBAL VARIABLES ***/

static MuzzleUI_Style __style;

/*** GLOBAL VARIABLES ***/

/*** FUNCTIONS ***/

static bool __mzui_internal_check_collision_point_rec(vec2 point, rectangle rec)
{
    if ((point.x >= rec.x) && (point.x <= (rec.x + rec.width)) && (point.y >= rec.y) && (point.y <= (rec.y + rec.height))) return true;
    return false;
}

void MuzzleUI_SetStyle(MuzzleUI_Style style);
MuzzleUI_Style MuzzleUI_GetStyle();

void MuzzleUI_UpdateButton(MuzzleUI_Button* button, Applet* applet);
void MuzzleUI_DrawButton(MuzzleUI_Button button);

/*** FUNCTIONS ***/

#endif // MUZZLEUI_H