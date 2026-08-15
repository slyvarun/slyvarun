<!-- ======================================================= -->
<!-- ================= AESTHETIC HEADER ==================== -->
<!-- ======================================================= -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:4285F4&height=130&section=header&text=Sai%20Varun%20Degala&fontSize=40&fontAlign=50&fontAlignY=40&desc=Abstracting%2520Intelligence&descAlign=50&descAlignY=65&fontColor=ffffff&descSize=16&animation=twinkling" width="100%" />
</div>

<br>

<!-- ======================================================= -->
<!-- ================= GITHUB TELEMETRY ==================== -->
<!-- ======================================================= -->
<div align="center">
  <h3 style="border-bottom: none; font-weight: 300; margin: 0 0 10px 0;"><code>// GITHUB_TELEMETRY</code></h3>
  <img src="https://github-readme-stats.shion.dev/api?username=slyvarun&theme=shadow_blue&hide_border=true&show_icons=true&include_all_commits=true&count_private=true" width="48%" style="max-width: 420px;" />
  &nbsp;&nbsp;
  <img src="https://streak-stats.demolab.com/?user=slyvarun&theme=shadow_blue&hide_border=true" width="48%" style="max-width: 420px;" />
</div>

<br>
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=4285F4&height=1" width="70%" />
</div>
<br>

<!-- ======================================================= -->
<!-- ================= MINI GAME: SKILL BLAST ============== -->
<!-- ======================================================= -->
<div align="center">
  <h3 style="border-bottom: none; font-weight: 300; margin: 0 0 5px 0;"><code>// LAUNCH_SKILL_BLAST</code></h3>
  <p style="font-size: 13px; color: #888; margin-bottom: 10px;">Click/Tap target blocks below to launch the rocket and uncover your arsenal!</p>

  <div id="game-container" style="position: relative; width: 100%; max-width: 500px; height: 180px; background: #0d1117; border: 1px solid #30363d; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; padding: 15px; box-sizing: border-box;">
    
    <!-- Score & Status Bar -->
    <div style="display: flex; justify-content: space-between; font-family: monospace; font-size: 12px; color: #4285F4;">
      <span id="game-score">UNLOCKED: 0 / 6</span>
      <span id="game-msg">STATUS: READY FOR LAUNCH</span>
    </div>

    <!-- Target Skill Blocks Grid -->
    <div id="skill-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; z-index: 2;">
      <div class="skill-tile" onclick="blastSkill(this, 'Python')" style="background: #161b22; border: 1px dashed #4285F4; border-radius: 6px; padding: 8px; cursor: pointer; text-align: center; font-family: monospace; font-size: 12px; color: #8b949e; transition: all 0.3s;">
        🔒 [CLASSIFIED]
      </div>
      <div class="skill-tile" onclick="blastSkill(this, 'PyTorch')" style="background: #161b22; border: 1px dashed #4285F4; border-radius: 6px; padding: 8px; cursor: pointer; text-align: center; font-family: monospace; font-size: 12px; color: #8b949e; transition: all 0.3s;">
        🔒 [CLASSIFIED]
      </div>
      <div class="skill-tile" onclick="blastSkill(this, 'FastAPI')" style="background: #161b22; border: 1px dashed #4285F4; border-radius: 6px; padding: 8px; cursor: pointer; text-align: center; font-family: monospace; font-size: 12px; color: #8b949e; transition: all 0.3s;">
        🔒 [CLASSIFIED]
      </div>
      <div class="skill-tile" onclick="blastSkill(this, 'Neo4j')" style="background: #161b22; border: 1px dashed #4285F4; border-radius: 6px; padding: 8px; cursor: pointer; text-align: center; font-family: monospace; font-size: 12px; color: #8b949e; transition: all 0.3s;">
        🔒 [CLASSIFIED]
      </div>
      <div class="skill-tile" onclick="blastSkill(this, 'Docker')" style="background: #161b22; border: 1px dashed #4285F4; border-radius: 6px; padding: 8px; cursor: pointer; text-align: center; font-family: monospace; font-size: 12px; color: #8b949e; transition: all 0.3s;">
        🔒 [CLASSIFIED]
      </div>
      <div class="skill-tile" onclick="blastSkill(this, 'TypeScript')" style="background: #161b22; border: 1px dashed #4285F4; border-radius: 6px; padding: 8px; cursor: pointer; text-align: center; font-family: monospace; font-size: 12px; color: #8b949e; transition: all 0.3s;">
        🔒 [CLASSIFIED]
      </div>
    </div>

    <!-- Rocket Launcher -->
    <div id="rocket" style="position: absolute; bottom: 5px; left: 50%; transform: translateX(-50%); font-size: 18px; transition: all 0.4s ease-in-out; pointer-events: none;">
      🚀
    </div>
  </div>
</div>

<script>
  let unlockedCount = 0;
  function blastSkill(element, skillName) {
    if (element.classList.contains('unlocked')) return;
    
    const rocket = document.getElementById('rocket');
    const msg = document.getElementById('game-msg');
    const containerRect = document.getElementById('game-container').getBoundingClientRect();
    const elemRect = element.getBoundingClientRect();
    
    // Move rocket toward target
    const relativeX = (elemRect.left + elemRect.width / 2) - (containerRect.left + containerRect.width / 2);
    rocket.style.transform = `translate(calc(-50% + ${relativeX}px), -90px)`;
    msg.innerText = `LAUNCHING AT: ${skillName}...`;

    setTimeout(() => {
      element.classList.add('unlocked');
      element.style.background = '#1f6feb33';
      element.style.borderColor = '#4285F4';
      element.style.color = '#ffffff';
      element.style.fontWeight = 'bold';
      element.innerHTML = `✨ ${skillName}`;
      
      unlockedCount++;
      document.getElementById('game-score').innerText = `UNLOCKED: ${unlockedCount} / 6`;

      // Reset rocket position
      rocket.style.transform = 'translateX(-50%)';

      if (unlockedCount === 6) {
        msg.innerText = 'STATUS: ARSENAL FULLY UNLOCKED!';
      } else {
        msg.innerText = 'STATUS: READY FOR LAUNCH';
      }
    }, 400);
  }
</script>

<br>

<!-- ======================================================= -->
<!-- ================= FOOTER BANNER ======================= -->
<!-- ======================================================= -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4285F4,100:000000&height=60&section=footer" width="100%" />
</div>
