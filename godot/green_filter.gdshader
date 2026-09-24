// green_filter.gdshader — zöldes "halloweeni" színfilter Godot 4.x-hez (2D és 3D-ben is működik).
//
// HASZNÁLAT (2D):
//   1. A fő jelenetben adj hozzá egy CanvasLayer-t, layer = 100.
//   2. Abba egy ColorRect-et, méret: "Full Rect" (anchors: teljes képernyő).
//   3. A ColorRect Material slotjába: New ShaderMaterial → Shader: ez a fájl.
//   4. A ColorRect mouse_filter = Ignore, hogy a gombok átjárhatók legyenek.
//
// HASZNÁLAT (3D): ugyanez egy ColorRect-tel egy CanvasLayerben — a hint_screen_texture
// a 3D renderelt képet is felveszi, így a filter az egész játékon érvényesül.
//
// FONTOS: a UI-t ne tedd a filter alá (a filter CanvasLayer layer-száma legyen
// nagyobb, mint a játékvilágé, de kisebb, mint a HUD-é).

shader_type canvas_item;
render_mode unshaded;

uniform sampler2D screen_tex : hint_screen_texture, repeat_disable, filter_linear;

// --- hangulat ---
uniform float strength : hint_range(0.0, 1.0) = 0.40;      // 0 = ki, 0.4 = este, 0.75 = kráter/legendás zóna
uniform vec3 tint : source_color = vec3(0.84, 1.10, 0.87); // zöld felé tolás
uniform float saturation : hint_range(0.0, 2.0) = 0.88;    // fakóbb világ -> a vér és a meteor-zöld kiugrik
uniform float lift : hint_range(0.0, 0.5) = 0.09;          // árnyékok felemelése
uniform vec3 lift_color : source_color = vec3(0.045, 0.115, 0.075); // a "derengő zöld" színe
uniform float vignette : hint_range(0.0, 1.0) = 0.28;

// --- opcionális extra ---
uniform float grain : hint_range(0.0, 0.2) = 0.03;         // filmszemcse, mobilon 0.0 ajánlott
uniform float time_scale : hint_range(0.0, 4.0) = 1.0;

float rand(vec2 co) {
	return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

void fragment() {
	vec3 c = texture(screen_tex, SCREEN_UV).rgb;

	// 1. telítettség
	float l = dot(c, vec3(0.2126, 0.7152, 0.0722));
	vec3 g = mix(vec3(l), c, saturation);

	// 2. színezet
	g *= tint;

	// 3. árnyékemelés zöldbe (ez adja a kísérteties hatást)
	float amt = lift * (1.0 - clamp(l, 0.0, 1.0));
	g = mix(g, lift_color, amt);

	// 4. vignetta
	float d = distance(SCREEN_UV, vec2(0.5)) / 0.7071;
	g *= 1.0 - vignette * smoothstep(0.45, 1.0, d);

	// 5. filmszemcse
	g += (rand(SCREEN_UV * vec2(1920.0, 1080.0) + TIME * time_scale) - 0.5) * grain;

	// 6. keverés az eredetivel az erősség szerint
	COLOR.rgb = mix(c, g, strength);
	COLOR.a = 1.0;
}
