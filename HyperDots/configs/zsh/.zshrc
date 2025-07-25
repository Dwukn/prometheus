# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Skip global compinit - oh-my-zsh will handle it
skip_global_compinit=1

export ZSH="$HOME/.oh-my-zsh"

# PATH exports - consolidated for efficiency
export PATH="$HOME/.nvm/versions/node/v20.18.2/bin:$PATH"
export PATH="$PATH:/home/dawu/.dotnet/tools:/snap/bin:$HOME/.local/bin"
export ANDROID_HOME="$HOME/System/Android/Sdk"
export PATH="$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
export DOTNET_ROOT=/usr/lib64/dotnet

# NVM lazy loading - only load when needed (major performance boost)
export NVM_DIR="$HOME/.nvm"
nvm() {
    unset -f nvm node npm npx
    [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
    nvm "$@"
}
node() {
    unset -f nvm node npm npx
    [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
    node "$@"
}
npm() {
    unset -f nvm node npm npx
    [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
    npm "$@"
}
npx() {
    unset -f nvm node npm npx
    [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
    npx "$@"
}

# Theme and plugins - keep minimal
# ZSH_THEME="gallifrey"
ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(
    history
    zsh-autosuggestions
    fzf
)

# Disable oh-my-zsh auto-update checks for faster startup
DISABLE_AUTO_UPDATE="true"
DISABLE_UPDATE_PROMPT="true"

# History settings - optimized
HISTFILE=~/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
setopt SHARE_HISTORY HIST_EXPIRE_DUPS_FIRST HIST_IGNORE_DUPS HIST_FIND_NO_DUPS HIST_REDUCE_BLANKS APPENDHISTORY

# Load oh-my-zsh
source $ZSH/oh-my-zsh.sh

# Completion optimization - cache and faster loading
zstyle ':completion:*' use-cache yes
zstyle ':completion:*' cache-path ~/.zsh/cache
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|=*' 'l:|=* r:|=*'

# Load FZF only if file exists
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Aliases - grouped for readability
# File operations
alias ls='exa --icons --group-directories-first'
alias ll='exa -la --icons --group-directories-first'
alias lt='exa -T --icons --level=2'
alias icat='kitten icat'

# Directory shortcuts
alias doc='cd ~/Personal/Documents/'
alias dow='cd ~/Personal/Downloads/'
alias pic='cd ~/Ted/Programming/'
alias gof='cd ~/Programming/go/'

# Git shortcuts
alias g='git'
alias gs='git status'
alias ga='git add'
alias gra='git remote add origin'
alias gcm='git commit -m'
alias gco='git checkout'
alias gbr='git branch'
alias gbl='git blame'
alias gpu='git push'
alias gpo='git push origin'
alias gpom='git push origin main'
alias gpl='git pull'
alias gd='git diff'
alias gl='git log --oneline --graph --decorate'
alias gls='git log --stat'
alias gcl='git clone'
alias gf='git fetch'
alias gr='git restore'
alias grs='git restore --staged'
alias grb='git rebase'

# Development shortcuts
alias nrd='npm run dev'
alias nrs='npm run start'
alias nrb='npm run build'
alias nrt='npm run test'

# Python virtual environments
alias 310='source ~/System/venvs/310/.venv/bin/activate'
alias 311='source ~/System/venvs/311/.venv/bin/activate'
alias 312='source ~/System/venvs/312/venvs/bin/activate'

# Utility aliases
alias poke='pokemon-colorscripts --no-title -s -n'
alias fast='fastfetch -c $HOME/.config/fastfetch/config-compact.jsonc'
alias rdb='rm ~/.cache/cliphist/db'
alias android-medium_phone='emulator -avd Medium_Phone_API_36.0'

# Load syntax highlighting last for better performance
[ -f ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ] && source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Load custom environment variables if they exist
[ -f "$HOME/.local/bin/env" ] && source "$HOME/.local/bin/env"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
