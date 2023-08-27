from autocoilgun import *

def activate_all_forwards(proj, stage):
    z_proj = proj.z_pos
    z_stage = stage.z_pos

    if z_proj > z_stage:
        return REDACTED
    else:
        return 0

def activate_one_forward(proj, stage):
    z_proj = proj.z_pos
    z_stage = stage.z_pos
    maxdist = stage.L * 1.5

    if z_proj - z_stage > 0 and z_stage + maxdist > z_proj:
        return REDACTED
    else:
        return 0

# loader params: idx, r_in, thickness, L, mtl, z_pos
# stage params: idx, N, L, r_in, D_wire, t_ext1, t_ext2, mtl_ext, z_pos
# projectile params: r, L, mtl, z_pos, vel, rho

# this is a 1.6 mm cannon with a muzzle velocity slight above 72 m/s
steel_density = 7870
loader = LoadingBlock(0, 1.6, 75, 100, "REDACTED", 100)
stage1 = Stage(# REDACTED
stage2 = Stage(# REDACTED
stage3 = Stage(# REDACTED
stage4 = Stage(# REDACTED
stage5 = Stage(# REDACTED
stage6 = Stage(# REDACTED
stage7 = Stage(# REDACTED
stage8 = Stage(# REDACTED
stage9 = Stage(# REDACTED
stages = [loader, stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8, stage9]
gun = Coilgun(stages)
proj = Projectile(# REDACTED
print("Projectile mass:", proj.mass*1000, "g")

# PerformAnalysisFull(gun, proj, activate_one_forward, "KST2", "KST2", 30, 3, 0.0025, 20)
# PerformAnalysisDiscretePosition(gun, proj, activate_one_forward, "KST2", "KST2", 30, 3, 20)
PerformAnalysisDiscreteTime(gun, proj, activate_one_forward, "KST2", "KST2", 30, 3, 0.0025)
