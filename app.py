from flask import Flask, render_template, request, redirect, url_for
from monitor import get_system_stats
from optimizer import suggest_optimizations
from process_killer import list_processes, kill_process
from optimizer import auto_kill_useless_processes

app = Flask(__name__)

@app.route('/')
def index():
    stats = get_system_stats()
    suggestions = suggest_optimizations(stats)
    processes = list_processes(limit=15)
    return render_template('index.html', stats=stats, suggestions=suggestions, processes=processes)

@app.route('/kill/<int:pid>', methods=['POST'])
def kill(pid):
    kill_process(pid)
    return redirect(url_for('index'))


@app.route('/auto_optimize')
def auto_optimize():
    auto_kill_useless_processes()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
