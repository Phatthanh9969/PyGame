 // On Mod Load:
#macro defammo 1

#define init
	global.newLevel = instance_exists(GenCont);
	global.nanner = sprite_add("nanner.png", 1,5,5);
	/// Define Sprites : sprite_add("path/to/sprite/starting/from/mod/location.png", frames, x-offset, y-offset) \\\
	 // A-Skin:
	global.spr_idle[0] = sprite_add("sprMutant1Idle.png",	4, 10, 10);
	global.spr_walk[0] = sprite_add("sprMutant1Walk.png",	6, 12, 12);
	global.spr_hurt[0] = sprite_add("sprMutant1Hurt.png",	3, 12, 12);
	global.spr_dead[0] = sprite_add("sprMutant1Dead.png",	6, 12, 12);
	global.spr_sit1[0] = sprite_add("sprMutant1GoSit.png",	3, 12, 12);
	global.spr_sit2[0] = sprite_add("sprMutant1Sit.png",	1, 12, 12);

	
	 // Character Selection / Loading Screen:
	global.spr_slct = sprite_add("sprCharSelect.png",	1,				0,  0);
	global.spr_port = sprite_add("sprBigPortrait.png",	race_skins(),	40, 243);
	global.spr_icon = sprite_add("sprMapIcon.png",		race_skins(),	5, 5);

	 // Ultras:
	global.spr_ultport[1] = sprite_add("ultra1.png", 1, 12, 16);
	global.spr_ultport[2] = sprite_add("ultra2.png", 1, 12, 16);
	global.spr_ult_icon[1] = sprite_add("sprEGIconHUDA.png", 1, 8, 9);
	global.spr_ult_icon[2] = sprite_add("sprEGIconHUDB.png", 1, 8, 9);


	var _race = [];
	for(var i = 0; i < maxp; i++) _race[i] = player_get_race(i);
	while(true){
		/// Character Selection Sound:
		for(var i = 0; i < maxp; i++){
			var r = player_get_race(i);
			if(_race[i] != r && r = "monkey"){

			}
			_race[i] = r;
		}

		/// Call level_start At The Start Of Every Level:
		if(instance_exists(GenCont)) global.newLevel = 1;
		else if(global.newLevel){
			global.newLevel = 0;
			level_start();
		}
		wait 1;
	}
	if(fork()){
        var gce = false;
        while 1{
            if instance_exists(GenCont) || instance_exists(menubutton){
                gce = true;
            }else{
                if (gce){
                	
                    with(instances_matching(Player,"race",mod_current)){
                        charammo = 1;
			cooldown = 0;
                    }
                }
                gce = false;
            }
            wait 0;
        }
        exit;
    }


 // On Level Start: (Custom Script, Look Above In #define init)
#define level_start

if(ultra_get(mod_current, 2)){
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,RadChest);}
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,AmmoChest);}
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,HealthChest);}
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,BigWeaponChest);}
}
if(instance_exists(Player)){
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,WeaponChest);}
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,AmmoPickup);}
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,HPPickup);}
}
if(skill_get(5)){
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,AmmoPickup);}
with(instances_matching(Player, "race", mod_current)){instance_create(x,y,HPPickup);}
}

 // On Run Start:
#define game_start



 // On Character's Creation (Starting a run, getting revived in co-op, etc.):
#define create

	 // Set Sprites:
	spr_idle = global.spr_idle[bskin];
	spr_walk = global.spr_walk[bskin];
	spr_hurt = global.spr_hurt[bskin];
	spr_dead = global.spr_dead[bskin];
	spr_sit1 = global.spr_sit1[bskin];
	spr_sit2 = global.spr_sit2[bskin];


	charammo = 1;
	cooldown = 150;
 // Every Frame While Character Exists:
#define step
{ // ACTIVE //
with (Player) {
if(race==mod_current){
	cooldown = max(0, cooldown - 1);
	
	if (cooldown == 0 && charammo == 0){
		charammo = 1;
		cooldown = 150;
		sound_play(sndSwapFlame);
	with (instance_create(x, y, PopupText)) {
		target = other.index;
		mytext = "@yCHARGED";
	}

	}
}
}
    if(usespec or (canspec and button_pressed(index, "spec"))) { // usin the active
        var typ = weapon_get_type(wep);
	if (charammo <= 0) {
	sound_play(sndEmpty);
	with (instance_create(x, y, PopupText)) {
		target = other.index;
		mytext = "@bCOOLDOWN";
	}

	exit;
} else charammo -= 1;
sound_play(sndConfetti1);
repeat(1) + (ultra_get(mod_current, 1) * 3) + (ultra_get(mod_current, 2) * 2)
with(instance_create(x,y,Grenade)){
sprite_index = global.nanner;
team = other.team;
creator = other;
direction = other.gunangle + (random_range(-10, 10) * other.accuracy);
image_angle = direction + (random_range(-50,50));
speed = 10;
damage = 5 + (ultra_get(mod_current, 1) * 3)
}
     }                             

}


 // Name:
#define race_name
	return "MONKEY";


 // Description:
#define race_text
	return "@gCARE PACKAGES#@yEXPLOSIVE BANANAS";


 // Starting Weapon:
#define race_swep
	return 1; // Revolver


 // Throne Butt Description:
#define race_tb_text
	return "@wBIGGER @gCARE PACKAGES";


 // On Taking Throne Butt:
#define race_tb_take


#define race_soundbank
return "chicken";

 // Character Selection Icon:
#define race_menu_button
	sprite_index = global.spr_slct;


 // Portrait:
#define race_portrait
	return global.spr_port;


 // Loading Screen Map Icon:
#define race_mapicon
	return global.spr_icon;


 // Skin Count:
#define race_skins
	return 1; // 2 Skins, A + B


 // Skin Icons:
#define race_skin_button
	sprite_index = global.spr_skin;
	image_index = argument0;


 // Ultra Names:
#define race_ultra_name
	switch(argument0){
		case 1: return "BANANA FRENZY";
		case 2: return "ARMED AND READY";
		/// Add more cases if you have more ultras!
	}


 // Ultra Descriptions:
#define race_ultra_text
	switch(argument0){
		case 1: return "@yMORE BANANAS @rHIGHER DAMAGE";
		case 2: return "@wTHE BEST @gCARE PACKAGES #@wSLIGHTLY BETTER @yBANANAS";
		/// Add more cases if you have more ultras!
	}


 // On Taking An Ultra:
#define race_ultra_take
	if(instance_exists(mutbutton)) switch(argument0){
		 // Play Ultra Sounds:
		case 1:	sound_play(sndChickenUltraA); break;
		case 2: sound_play(sndChickenUltraB); break;
		/// Add more cases if you have more ultras!
	}


 // Ultra Button Portraits:
#define race_ultra_button
sprite_index = global.spr_ultport[argument0];


 // Ultra HUD Icons:
#define race_ultra_icon
	return global.spr_ult_icon[argument0];



 // Loading Screen Tips:
#define race_ttip
	return ["MONKEYING AROUND", "GOING BANANAS", "BANANA CARE PACKAGE", "YO", "JUMPING ON THE BED", "NANNERS"];