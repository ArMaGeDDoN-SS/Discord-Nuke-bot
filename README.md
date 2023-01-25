<p align="center" dir="auto"><img src="https://media.discordapp.net/attachments/1056974871764140062/1062740227497676810/Discord.py_Logo.png?width=1200&height=408" style="max-width: 100%;"></p>

<h1 align="center"> [Discord] - Biohazard: Standart Nuke-bot </h1>

<p align="center" dir="auto"><a href="https://github.com/ArMaGeDDoN-SS/Standard-Nuke-bot/blob/main/README.md"><img src="https://img.shields.io/github/downloads/ArMaGeDDoN-SS/Discord-Nuke-bot/total?logo=GitHub&style=flat-square" style="max-width: 100%;"></a> <a href="https://discord.gg/yxJSYaQc2F"><img src="https://img.shields.io/discord/1055522427272175646?color=15315c&label=Discord%20Server&logo=discord&logoColor=fff&style=flat-square" style="max-width: 100%;"></a> <img src="https://img.shields.io/github/languages/code-size/ArMaGeDDoN-SS/Discord-Nuke-bot?color=ad3434&logo=Python&logoColor=fff&style=flat-square"> <img src="https://img.shields.io/github/watchers/ArMaGeDDoN-SS/Discord-Nuke-bot?color=772694&logo=WeChat&logoColor=fff&style=flat-square"> <a href="https://www.youtube.com/channel/UCvphtiRwg79OYUguZBJvGJQ"><img src="https://img.shields.io/youtube/channel/subscribers/UCvphtiRwg79OYUguZBJvGJQ?label=YouTube%20channel&logo=youtube&logoColor=fff&style=flat-square"></a></p><p align="center" dir="auto"><a href="https://discordpy.readthedocs.io/en/stable/index.html"><img src="https://img.shields.io/pypi/v/discord.py?color=FCCB34&label=Discord.Py&logo=Battle.net&logoColor=668FB7&style=for-the-badge" style="max-width: 100%;"></a></p> <p align="center" dir="auto">[Discord] - Biohazard is a bot designed to destroy Discord servers. Written in Python 3.9, the code is sorted into kogi for convenience.</p> <p align="center" dir="auto">This nuke bot contains a total of 21 commands, all of them created to destroy the server where this command was registered. In addition to two commands, the bot also contains 2 events (a reaction to the creation of channels, a team cooldown). The bot also provides a help that provides information about all the commands of the bot.</p>

<h2 align="center" dir="auto"><a id="user-content-disclaimer" class="anchor" aria-hidden="true" href="#disclaimer"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Disclaimer!</h2>


<table style='font-family:"Courier New", Courier, monospace; font-size:80%' align="center">
  <thead>
    <tr>
      <th align="center"> This bot was created solely for entertainment and educational purposes </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"> The use and development of such bots contradicts Discord T.O.S</td>
    </tr>
    <tr>
      <td align="center"> By using this bot, you automatically confirm that you are fully responsible for its further use. If your account is blocked by discord support for using this bot, I will not be held responsible. </td>
    </tr>
  </tbody>
</table>

<h1 align="center" dir="auto"><a id="user-content-disclaimer" class="anchor" aria-hidden="true" href="#disclaimer"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>How To Setup - Instructions</h1>

<p> <b>Before you start using the bot, please change its configuration settings via the "config.json" JSON file.Be sure to insert your future bot's token in the right place in the json dictionary (you can get your bot's token on the <a href="https://discord.com/developers">Discord Developers website</a>).</b> </p>

```json
{
	"token": "Your bot token",
	"prefix": "YOU PREFIX HERE",
	"loghook": "The webhook to which information about the destroyed servers will be sent.", 
	"developer_list": ["List of people who will be granted access to the developer's commands"],
	"channels_name": "The names of the channels that the bot will create during the destruction",
	"roles_name": "The names of the roles that the bot will create during the destruction",
	"server_name": "The name to which the name of the server will be changed before the destruction",
	"avatar_file": "avatar.jpg (The file name is avatars. It is necessary to change the server avatar)",
}
```
<p> <b> Information about each line of the "config.json" file: </b> </p>
<ul>
<li><p><code>token</code> - This line specifies the token of your bot. You can get your bot token on the official Discord Developers website.</p></li>
<li><p><code>prefix</code> - This line specifies the prefix of your bot. The default value is <code>"!"</code>.</p></li>
<li><p><code>loghook</code> - This line contains a link to the webhook to which information about the target server is sent.</p></li>
<li><p><code>developer_list</code> - This list specifies the ID of users who will have access to system commands that edit the blacklist and whitelist.</p></li>
<li><p><code>channels_name</code> - This line specifies the name for the channels that the bot will spam when the server is destroyed.</p></li>
<li><p><code>roles_name</code> - This line specifies the name for the roles that the bot will spam when the server is destroyed.</p></li>
<li><p><code>server_name</code> - This line specifies a new name for the server. When the bot destroys the server, it changes its name to the specified one.</p></li>
<li><p><code>avatar_file</code> - This line specifies the name of the avatar file. During the destruction of the server, the bot changes its avatar.</p></li>
</ul>

<h1 align="center" dir="auto"><a id="user-content-disclaimer" class="anchor" aria-hidden="true" href="#disclaimer"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>List of commands</h1>

<p align="center">
	<strong> To view a list of all bot commands, enter the <code>documentation</code> command in the chat of any server where there is a bot (do not forget to specify the prefix before the command name), the bot will send you a list of all available commands to the bos. The name of the file where the <code>documentation</code> command is stored: <a href="">system_bot.py</a> </strong>
</p>

<p align="center"><img src="https://media.discordapp.net/attachments/1052941656564961291/1063176944541257798/image.png?width=883&height=555" align="center"></p>

<p align="center" style="font-size:2">
	<small><i> Visual view of the command <code>documentation</code> </i></small>
</p>

<p>
	<strong>Here is a handy list of all the commands with a description of their functionality, which are currently available and successfully working in the bot version <code>1.0.1</code>:</strong>
</p>

<details>
<summary>General commands</summary>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto">
	
```C#
+ attack - Automatic server destruction.
+ delchannels - Deleting all channels.
+ delroles - Deleting all roles.
+ channels - Mass creation of channels.
+ roles - Mass creation of roles.
+ rename - Changing the server name.
+ delemoji - Deleting all emojis.
```
</div>
</details>

<details>
<summary>Commands for interacting with server participants</summary>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto">
	
```C#
+ kick_all - Kick all participants.
+ ban_all - Ban all participants.	
```
</div>
</details>

<details>
<summary>Commands for interacting with roles</summary>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto">
	
```C#
+ admin - Give yourself a role with administrator rights.
+ everyone_admin - Grant administrator rights to all participants.
+ giverole <@Ping role | ID role> - Give yourself the mentioned role.	
```
</div>
</details>

<details>
<summary>Spam commands</summary>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto">
	
```C#
+ spam - Mass sending of messages to the channels.
+ allspam - Mass sending of messages to all channels.
+ dmspam <@пинг | ID> - Mass sending of messages to the mentioned.
```
</div>
</details>
	
<details>
<summary>Custom classic nuke-commands</summary>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto">
	
```C#
+ customchan <Name> - Mass creation of channels with the specified name.
+ customroles <Name> - Mass creation of roles with the specified name.
+ customname <Name> - Changing the server name to the specified one.
+ customspam <Text> - Mass spam with the specified text.
```
</div>
</details>

<details>
<summary>Quantitatively custom nuke-commands</summary>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto">
	
```C#
+ intchannels <Number> - Creating the specified number of channels.
+ introles <Number> - Creating the specified number of roles.
```
</div>
</details>
